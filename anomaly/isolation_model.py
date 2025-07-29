from sklearn.ensemble import IsolationForest
import numpy as np
import joblib
import os

class AnomalyDetector:
    def __init__(self, model_path='anomaly_model.pkl'):
        self.model_path = model_path
        if os.path.exists(model_path):
            self.model = joblib.load(model_path)
        else:
            self.model = IsolationForest(contamination=0.02, random_state=42)

    def train(self, embeddings):
        """Train the model on a list of embeddings"""
        self.model.fit(embeddings)
        joblib.dump(self.model, self.model_path)

    def score(self, embedding):
        """Return anomaly score and flag"""
        score = self.model.decision_function([embedding])[0]
        is_anomaly = self.model.predict([embedding])[0] == -1
        return score, is_anomaly
