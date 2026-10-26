"""
App:
It takes a sentence as imput and tells whether the sentiment is positive or negative

"""
from transformers import pipeline
sentiment_analyzer = pipeline(
    "sentiment-analysis",
    model = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)
text = input("Enter a sentence: ")
result = sentiment_analyzer(text)
print("\n Sentiment Result: ")
print("Label: ",result[0]['label'])
print("Score: ",result[0]['score'])
