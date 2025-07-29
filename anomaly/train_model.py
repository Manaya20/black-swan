import numpy as np
from anomaly.isolation_model import AnomalyDetector

normal_data = np.random.normal(0, 0.2, (200, 384))  

detector = AnomalyDetector()
detector.train(normal_data)
print("✅ Isolation Forest trained and saved.")