from kafka import KafkaProducer
import json
import time
import os
import tweepy
from dotenv import load_dotenv

load_dotenv()
bearer_token = os.getenv("BEARER_TOKEN")

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

client = tweepy.Client(bearer_token=bearer_token)

def fetch_tweets():
    response = client.search_recent_tweets(query="war OR crash OR inflation", max_results=10)
    if response.data:
        for tweet in response.data:
            msg = {"text": tweet.text, "id": tweet.id}
            producer.send('tweets', value=msg)
            print("→ Tweeted:", tweet.text[:80])

if __name__ == "__main__":
    while True:
        fetch_tweets()
        time.sleep(60)
