# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy code
COPY src/ ./src/
COPY linear_model.joblib .

# Install dependencies
RUN pip install scikit-learn joblib

# Default command to run prediction
CMD ["python", "src/predict.py"]

