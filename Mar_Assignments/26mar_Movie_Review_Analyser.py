from textblob import TextBlob
reviews = [
    "This movie is amazing and fantastic!",
    "I really loved the story and acting",
    "The movie was okay, not great",
    "It was boring and too long",
    "Worst movie ever, waste of time"
]
for review in reviews:
    analysis = TextBlob(review)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        sentiment = "Positive 😊"
    elif polarity == 0:
        sentiment = "Neutral 😐"
    else:
        sentiment = "Negative 😠"
    print("Review:", review)
    print("Sentiment:", sentiment)
    print("-" * 40)