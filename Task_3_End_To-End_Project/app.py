from flask import Flask, request, jsonify
import pickle
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load trained model from file
try:
    model = pickle.load(open("titanic_model.pkl", "rb"))
except FileNotFoundError:
    raise Exception("⚠️ 'titanic_model.pkl' not found in project directory.")

# Define a basic route
@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the Titanic Survival Prediction API! Use the /predict endpoint with POST."
    })

# Define prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Ensure all required fields are present
        required = ['Pclass', 'Sex', 'Age']
        if not all(field in data for field in required):
            return jsonify({"error": f"Missing one of {required}"}), 400

        # Prepare input for model
        features = np.array([[data['Pclass'], data['Sex'], data['Age']]])
        prediction = model.predict(features)[0]

        return jsonify({
            "prediction": int(prediction),
            "survived": bool(prediction)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the app (local testing)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)