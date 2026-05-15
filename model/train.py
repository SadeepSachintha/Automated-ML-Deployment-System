import os
import joblib
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_model():
    print("Loading Iris dataset...")
    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    y = iris.target

    print("Splitting dataset...")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("Training Random Forest Classifier...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    print("Evaluating model...")
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Model Accuracy: {accuracy:.4f}")

    # Ensure app directory exists to save the model
    # When deployed, the model will be read by the API in the app directory
    os.makedirs(os.path.join(os.path.dirname(__file__), '..', 'app', 'model_data'), exist_ok=True)
    model_path = os.path.join(os.path.dirname(__file__), '..', 'app', 'model_data', 'model.joblib')
    
    print(f"Saving model to {model_path}...")
    joblib.dump(model, model_path)
    print("Training complete and model saved.")

if __name__ == "__main__":
    train_model()
