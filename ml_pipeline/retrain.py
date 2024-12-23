import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import joblib

def preprocess_data(filepath):
    df = pd.read_csv(filepath)
    x = df.drop(columns = df[['price_range']])
    y = df['price_range']
    return x, y

def retrain_model(new_data_path):

    model_path = "./models/knn_model1.pkl"
    model = joblib.load(model_path)
    X_new, y_new = preprocess_data(new_data_path)
    model.fit(X_new, y_new)
    joblib.dump(model, model_path)
    print("Model retrained and saved successfully.")

if __name__ == "__main__":
    import sys
    new_data_path = sys.argv[1]
    retrain_model(new_data_path)