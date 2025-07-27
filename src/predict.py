import joblib
import numpy as np

# Load saved model
model = joblib.load("linear_model.joblib")

# Sample dummy data (same feature count as training data)
dummy_input = np.array([[8.3252, 41.0, 6.984127, 1.02381, 322.0, 2.555556, 37.88, -122.23]])
prediction = model.predict(dummy_input)

print(f"Sample prediction: {prediction[0]}")

