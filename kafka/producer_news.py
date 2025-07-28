from kafka import KafkaProducer
import feedparser
import time
import json

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

RSS_FEED = "https://feeds.a.dj.com/rss/RSSWorldNews.xml"

def fetch_news():
    feed = feedparser.parse(RSS_FEED)
    for entry in feed.entries:
        data = {
            "title": entry.title,
            "summary": entry.summary,
            "published": entry.published
        }
        producer.send('news', value=data)
        print("→ Published:", entry.title)

if __name__ == "__main__":
    while True:
        fetch_news()
        time.sleep(60)  # every 1 minute
