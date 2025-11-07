import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from textblob import TextBlob
import time

# =========================
# Sentiment Logic
# =========================
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.1:
        sentiment = "Positive"
        scores = {"Positive": 100, "Neutral": 0, "Negative": 0}
    elif polarity < -0.1:
        sentiment = "Negative"
        scores = {"Positive": 0, "Neutral": 0, "Negative": 100}
    else:
        sentiment = "Neutral"
        scores = {"Positive": 0, "Neutral": 100, "Negative": 0}

    return sentiment, scores


# =========================
# Page Config
# =========================
st.set_page_config(page_title="AI Sentiment Analyzer", page_icon="🧠", layout="centered")

# =========================
# Theme Toggle (icon only)
# =========================
if "theme" not in st.session_state:
    st.session_state.theme = "dark"

# Small icon button in corner
col1, col2 = st.columns([9, 1])
with col2:
    if st.button("🌙" if st.session_state.theme == "dark" else "🌞", help="Toggle Theme"):
        st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

# =========================
# CSS for themes
# =========================
if st.session_state.theme == "dark":
    background = """
    <style>
    @keyframes gradientShift {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }
    .stApp {
        background: linear-gradient(270deg, #0f0f0f, #1a1a1a, #0f2027);
        background-size: 600% 600%;
        animation: gradientShift 12s ease infinite;
        color: white;
    }
    </style>
    """
else:
    background = """
    <style>
    .stApp {
        background: linear-gradient(180deg, #ffffff, #f3f4f6);
        color: black;
    }
    </style>
    """

st.markdown(background, unsafe_allow_html=True)

# =========================
# Common UI Styles
# =========================
st.markdown(
    """
    <style>
    .main-title {
        text-align: center;
        font-size: 2.8em;
        font-weight: 700;
        background: linear-gradient(90deg, #ff4d4d, #ffb84d, #57e389);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-top: 0.3em;
    }
    .subtext {
        text-align: center;
        font-size: 1.1em;
        opacity: 0.9;
        margin-bottom: 1.5em;
    }
    .result-box {
        border-radius: 10px;
        padding: 12px;
        text-align: center;
        font-weight: bold;
        color: white;
        margin-top: 20px;
    }
    .positive { background-color: #16a34a; }
    .neutral { background-color: #ca8a04; }
    .negative { background-color: #dc2626; }
    .stButton>button {
        background: linear-gradient(90deg, #ff4d4d, #ffb84d);
        color: white;
        border: none;
        padding: 0.6em 1.2em;
        border-radius: 8px;
        font-weight: 600;
        cursor: pointer;
        transition: 0.3s ease;
    }
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0px 0px 15px rgba(255, 255, 255, 0.3);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# =========================
# Header
# =========================
st.markdown("<h1 class='main-title'>🧠 AI Sentiment Analyzer</h1>", unsafe_allow_html=True)
st.markdown(
    "<p class='subtext'>Analyze your text to find if it’s "
    "<b style='color:#57e389;'>Positive</b>, "
    "<b style='color:#ff6b6b;'>Negative</b>, or "
    "<b style='color:#ffd93d;'>Neutral</b>.</p>",
    unsafe_allow_html=True,
)

# =========================
# Input Section
# =========================
user_input = st.text_area(
    "💬 Enter your sentence:",
    placeholder="Type something like: I love learning AI!",
    height=100,
)

# =========================
# Run Analysis
# =========================
if st.button("🔍 Analyze Sentiment", use_container_width=True):
    if user_input.strip():
        with st.spinner("Analyzing..."):
            time.sleep(1)
            sentiment, result = analyze_sentiment(user_input)

        sentiment_class = sentiment.lower()
        emoji = {"Positive": "😊", "Negative": "😠", "Neutral": "😐"}[sentiment]

        st.markdown(
            f"<div class='result-box {sentiment_class}'>{emoji} Sentiment: {sentiment}</div>",
            unsafe_allow_html=True,
        )

        # Pie chart
        labels = list(result.keys())
        sizes = list(result.values())
        colors = ["#57e389", "#ffd93d", "#ff6b6b"]

        fig, ax = plt.subplots(figsize=(5, 5))
        wedges, texts, autotexts = ax.pie(
            sizes,
            autopct="%1.1f%%",
            startangle=90,
            colors=colors,
            textprops={"fontsize": 11, "color": "white"},
        )

        plt.setp(autotexts, size=12, weight="bold")
        ax.legend(
            handles=[
                mpatches.Patch(color="#57e389", label="Positive 😊"),
                mpatches.Patch(color="#ffd93d", label="Neutral 😐"),
                mpatches.Patch(color="#ff6b6b", label="Negative 😠"),
            ],
            loc="upper center",
            bbox_to_anchor=(0.5, -0.05),
            ncol=3,
            fontsize=11,
            frameon=False,
            labelcolor="white" if st.session_state.theme == "dark" else "black",
        )

        ax.axis("equal")
        st.pyplot(fig)

        st.markdown("<hr>", unsafe_allow_html=True)
        st.caption("🚀 Built with ❤️ using Streamlit & TextBlob | by Jenil Gohel")
    else:
        st.warning("Please enter a sentence to analyze.")
