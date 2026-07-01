from flask import Flask, render_template, request
import pandas as pd
import pickle
import os

# Generate model if it doesn't exist
if not os.path.exists("model.pkl") or not os.path.exists("columns.pkl"):
    import train_model

app = Flask(__name__)

# Load model and feature columns
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("columns.pkl", "rb") as f:
    columns = pickle.load(f)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    year = int(request.form["year"])
    km_driven = int(request.form["km_driven"])
    fuel = request.form["fuel"]
    seller_type = request.form["seller_type"]
    transmission = request.form["transmission"]
    owner = request.form["owner"]
    brand = request.form["brand"]

    data = pd.DataFrame({
        "year": [year],
        "km_driven": [km_driven],
        "brand": [brand],
        "fuel": [fuel],
        "seller_type": [seller_type],
        "transmission": [transmission],
        "owner": [owner]
    })

    data = pd.get_dummies(
        data,
        columns=[
            "brand",
            "fuel",
            "seller_type",
            "transmission",
            "owner"
        ],
        drop_first=True
    )

    # Add missing columns
    for col in columns:
        if col not in data.columns:
            data[col] = 0

    # Arrange columns in correct order
    data = data[columns]

    prediction = model.predict(data)[0]

    return render_template(
        "index.html",
        prediction_text=f"Predicted Car Price: ₹ {prediction:,.2f}"
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
