from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
from sentence_transformers import SentenceTransformer
import spacy
import nltk
import re

sentiment_model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")
tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
sentiment_pipe = pipeline("sentiment-analysis", model=sentiment_model, tokenizer=tokenizer)

embedder = SentenceTransformer("paraphrase-MiniLM-L6-v2")
ner = spacy.load("en_core_web_sm")

def clean_text(text):
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^A-Za-z0-9 ]+", "", text)
    return text.strip().lower()

def get_sentiment(text):
    return sentiment_pipe(text[:512])[0]  

def get_embedding(text):
    return embedder.encode([text])[0]

def get_entities(text):
    doc = ner(text)
    return list(set([ent.label_ + ":" + ent.text for ent in doc.ents]))

def process_message(msg):
    text = msg.get("text") or msg.get("title") or ""
    cleaned = clean_text(text)
    sentiment = get_sentiment(cleaned)
    embedding = get_embedding(cleaned)
    entities = get_entities(cleaned)

    return {
        "text": text,
        "sentiment": sentiment["label"],
        "score": sentiment["score"],
        "entities": entities,
        "embedding": embedding.tolist() 
    }
