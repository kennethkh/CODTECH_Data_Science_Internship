# Task 3: End-to-End Machine Learning Project with Flask API

This project demonstrates how to build, save, and deploy a machine learning model as a REST API using Flask. It forms part of the CODTECH Data Science Internship.

---

## 🧠 Problem Statement

Using the Titanic dataset, we trained a Logistic Regression model to predict whether a passenger survived based on:
- Passenger class (`Pclass`)
- Sex (encoded: 0 = male, 1 = female)
- Age

---

## ⚙️ Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- Pickle
- Render (for deployment)

---

## 📁 Folder Structure

---

## 🚀 How It Works

- `app.py` loads the trained model (`titanic_model.pkl`)
- Exposes an API endpoint at `/predict`
- Accepts POST requests with JSON input:
```json
{
  "Pclass": 3,
  "Sex": 0,
  "Age": 22
}

Returns JSON response: 

{
  "prediction": 0,
  "survived": false
}
