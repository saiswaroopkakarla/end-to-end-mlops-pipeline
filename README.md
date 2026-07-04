# End-to-End MLOps Pipeline

A branch-based MLOps learning project demonstrating the progressive evolution of a machine learning workflow, from raw model training to fully containerised, CI/CD-automated deployment.

Built on the **California Housing dataset** using `scikit-learn` Linear Regression.

---

## Branch Structure

This repo is organised as a progression of MLOps maturity stages, each on its own branch:

| Branch | Stage | What it adds |
|---|---|---|
| `dev` | Model development | Training script, model serialisation with `joblib` |
| `docker_ci` | Containerisation + CI/CD | Dockerfile, predict script, GitHub Actions pipeline |

> `main` holds this README. Checkout individual branches to explore each stage.

---

## Stage 1  Model Development (`dev` branch)

**Files:** `src/train.py`

Trains a Linear Regression model on the California Housing dataset and serialises it to disk.

```bash
git checkout dev
pip install scikit-learn joblib
python src/train.py
```

**Output:**
```
R² Score: 0.6062
Model saved to linear_model.joblib
```

---

## Stage 2 Docker + CI/CD (`docker_ci` branch)

**Files:** `src/train.py`, `src/predict.py`, `Dockerfile`, `.github/workflows/ci.yml`

Extends Stage 1 with:
- A `predict.py` script that loads the saved model and runs inference on sample data
- A `Dockerfile` that packages the pipeline into a portable container
- A GitHub Actions workflow that automates train → build → test → push to Docker Hub on every push to this branch

```bash
git checkout docker_ci
```

### Run locally

```bash
# Train and save model
python src/train.py

# Build Docker image
docker build -t saiswaroopkakarla/mlops-pipeline:latest .

# Run prediction inside container
docker run saiswaroopkakarla/mlops-pipeline:latest
```

**Expected output:**
```
Sample prediction: 4.151
```

### CI/CD Pipeline (GitHub Actions)

The `ci.yml` workflow triggers on every push to `docker_ci` and runs these steps automatically:

```
Checkout → Set up Python → Install deps → Train model
→ Build Docker image → Run container → Push to Docker Hub
```

> **Secrets required:** Set `DOCKER_USERNAME` and `DOCKER_PASSWORD` in your GitHub repository secrets for the push step to work.

---

## Tech Stack

| Tool | Purpose |
|---|---|
| `scikit-learn` | Linear Regression model |
| `joblib` | Model serialisation |
| `Docker` | Containerised inference |
| `GitHub Actions` | CI/CD automation |
| California Housing dataset | Training data (via `sklearn.datasets`) |

---

## Model Performance

| Metric | Value |
|---|---|
| R² Score | 0.6062 |
| Dataset | California Housing (20,640 samples, 8 features) |
| Model | Linear Regression |
| Train/Test split | 80/20 |

---

## Learning Objectives

This project covers:

- Reproducible model training and serialisation
- Writing modular `train.py` / `predict.py` separation of concerns
- Packaging ML code in Docker for environment-independent deployment
- Automating the full train → build → deploy cycle with GitHub Actions
- Managing Docker Hub credentials securely via GitHub Secrets

---

## Author

**Kakarla Sai Swaroop**  
M25DE1023 IIT Jodhpur, M.Tech Data Engineering
