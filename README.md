# 🚀 Automated ML Deployment System

A production-ready, fully automated end-to-end Machine Learning pipeline. This system automates the training of a Random Forest model on the Iris dataset and deploys it as a containerized API to **Hugging Face Spaces** using **GitHub Actions**.

## 🏗️ Architecture
1. **GitHub Actions**: Triggers on every push to `main`.
2. **Auto-Training**: The pipeline installs dependencies and runs `model/train.py` to generate an updated `model.joblib`.
3. **Seamless Deployment**: The system uses the `huggingface_hub` API to push the latest code and model to Hugging Face Spaces.
4. **FastAPI Serving**: The model is served via a FastAPI backend running inside a Docker container.

## 🛠️ Tech Stack
- **Languages**: Python 3.10
- **ML Frameworks**: Scikit-Learn, Pandas
- **API Framework**: FastAPI, Uvicorn
- **CI/CD**: GitHub Actions
- **Containerization**: Docker
- **Deployment**: Hugging Face Spaces

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- A Hugging Face account and a Space created with the **Docker SDK**.
- A GitHub repository for your code.

### GitHub Secrets Configuration
To enable the automated deployment, add the following secret to your GitHub repository:
- `HF_TOKEN`: Your Hugging Face "Write" Access Token.

## 📡 API Endpoints

### 1. Health Check
`GET /health`
Verifies if the model is loaded and the API is ready.

### 2. Prediction
`POST /predict`
Submit features to get a species prediction.

**Request Body:**
```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

**Response:**
```json
{
  "prediction": 0,
  "species": "setosa"
}
```

## 📂 Project Structure
- `app/`: FastAPI application code.
- `model/`: Training scripts and model definitions.
- `.github/workflows/`: CI/CD pipeline configuration.
- `Dockerfile`: Container configuration for production.