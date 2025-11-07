import pandas as pd
import os

os.makedirs("data", exist_ok=True)

data = {
    "text": [
        "I love this product, it's amazing!",
        "Absolutely horrible experience.",
        "The movie was fantastic, I enjoyed it.",
        "This is the worst service ever.",
        "It’s okay, not bad but not great.",
        "I’m so happy with my purchase!",
        "I hate waiting so long for delivery.",
        "Decent experience overall."
    ],
    "sentiment": [
        "positive", "negative", "positive", "negative",
        "neutral", "positive", "negative", "neutral"
    ]
}

df = pd.DataFrame(data)
df.to_csv("data/reviews.csv", index=False)
print("✅ Dataset saved to data/reviews.csv")
