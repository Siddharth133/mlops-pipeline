# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import joblib
# import numpy as np
# app = Flask(__name__)
# CORS(app) 
# @app.route("/predict", methods=['POST'])
# def predict():
#     data = request.json
#     model = joblib.load(r"S:\Mlops\ml_pipeline\model\knn_model1.pkl")
#     data = np.array(list(data.values()), dtype=float)
#     data = data.reshape(1, -1)
#     output = model.predict(data)
#     result = {"prediction": output.tolist()}
#     return jsonify(result)

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=5000)


import mlflow
import mlflow.sklearn
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

app = Flask(__name__)
CORS(app)

mlflow.set_tracking_uri("http://docker-mlflow-1:5001")

@app.route("/predict", methods=['POST'])
def predict():
    data = request.json
    print("Received data:", data)
    
    
    model = joblib.load("./model/knn_model1.pkl")
    
    
    try:
        data = np.array(list(data.values()), dtype=float)
        data = data.reshape(1, -1)
    except ValueError as e:
        return jsonify({"error": f"Invalid data format: {str(e)}"}), 400
    
    
    with mlflow.start_run():
        mlflow.log_param("num_features", len(data))  
        mlflow.log_param("model_type", "KNN")  
        
        
        output = model.predict(data)
        
        
        mlflow.log_metric("prediction_value", float(output[0]))  
        
        
        mlflow.sklearn.log_model(model, "knn_model") 

        result = {"prediction": float(output[0])}
    
    return jsonify(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5011)
