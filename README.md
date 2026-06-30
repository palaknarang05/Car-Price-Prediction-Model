# Car Price Prediction System

## Overview

This project is a machine learning-based web application that predicts the selling price of a used car based on user-provided input features. The system uses a supervised learning regression model trained on a car dataset and is deployed using a Flask web application.

The user interacts with a simple web interface, enters car details, and receives a predicted price instantly.

---

## Features

- Predicts used car prices using machine learning
- Web-based user interface using Flask
- Handles categorical and numerical input features
- Trained regression model using Scikit-learn
- Local deployment on Flask server

---

## Tech Stack

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- HTML, CSS
- Pickle for model serialization

---

## Project Structure

CarPricePrediction/
│── app.py                # Flask application
│── train_model.py        # Model training script
│── car_data.csv          # Dataset used for training
│── templates/
│     └── index.html      # Frontend UI
│── requirements.txt      # Project dependencies
│── .gitignore

---

## How to Run the Project

### 1. Clone the repository
git clone https://github.com/palaknarang05/Car-Price-Prediction-Model.git
cd Car-Price-Prediction-Model

---

### 2. Create virtual environment
python -m venv venv

source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows

---

### 3. Install dependencies
pip install -r requirements.txt

---

### 4. Train the model
Since model files are not included in the repository, they must be generated locally:

python train_model.py

This will generate:
- model.pkl
- columns.pkl

---

### 5. Run the Flask application
python app.py

---

### 6. Open in browser
http://127.0.0.1:5000/

---

## Input Features

The model takes the following inputs:

- Brand
- Manufacturing Year
- Kilometers Driven
- Fuel Type
- Seller Type
- Transmission Type
- Owner Type

---

## Output

The system predicts the estimated selling price of the car based on the input features.

---

## Machine Learning Model

- Type: Regression Model
- Algorithm: Scikit-learn regression algorithm
- Approach: Supervised learning
- Model serialization: Pickle

---

## Note

- The virtual environment (venv), cache files, and model files are excluded from the repository.
- The model is generated locally using the training script.

---

## Future Improvements

- Deploy the application on cloud platforms like Render or Railway
- Improve model accuracy with feature engineering
- Enhance UI using Bootstrap or React
- Add authentication system for users

---

## Author

Palak Narang
GitHub: https://github.com/palaknarang05
