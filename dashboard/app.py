import streamlit as st
from nlp.processor import process_message
from anomaly.isolation_model import AnomalyDetector
import random

detector = AnomalyDetector()

messages = [
    {"text": "Markets tumble after war breaks out in Europe."},
    {"text": "The Fed holds interest rates steady amid cooling inflation."},
    {"text": "Explosion in tech hub causes panic in investor circles."},
    {"text": "Amazon announces record profits amid global recession."}
]

st.set_page_config(page_title="Black Swan Detector", layout="centered")
st.title("🧠 Real-Time Black Swan Detector")

for msg in messages:
    processed = process_message(msg)
    score, is_anomaly = detector.score(processed["embedding"])

    st.markdown(f"### 🗞️ {processed['text'][:80]}")
    col1, col2, col3 = st.columns(3)

    col1.metric("📉 Sentiment", processed["sentiment"])
    col2.metric("⚠️ Anomaly Score", round(score, 4), delta=None)
    col3.metric("🚨 Alert", "Yes" if is_anomaly else "No")

    if is_anomaly:
        st.error("🚨 Black Swan Detected!")
    else:
        st.success("✅ Normal")

    st.markdown("---")
