from nlp.processor import process_message

sample = {
    "text": "Breaking: The Federal Reserve raises interest rates again amid inflation fears."
}

result = process_message(sample)
print("Sentiment:", result["sentiment"], "| Score:", result["score"])
print("Entities:", result["entities"])
print("Embedding Dim:", len(result["embedding"]))
