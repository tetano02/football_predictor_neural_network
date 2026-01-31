# ⚽ Football Predictor Neural Network

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-orange)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A neural network–based project designed to predict **Serie A football match outcomes** by combining **historical match data**, **team market values**, and **recent performance trends**.

---

## 📌 Project Goal

The goal of this project is to predict football match outcomes using a **binary classification approach**:

- **1X** → Home win or draw  
- **X2** → Away win or draw  

The model leverages:
- Historical match results
- Team market values as a proxy for squad strength
- Short-term form based on the last 5 matches

---

## 🧠 Key Features

- Multi-season historical dataset (2013–2023)
- Market value integration from Transfermarkt
- Trend-based performance modeling
- Neural network implemented with **Keras**
- Strong generalization on unseen data

---

## 📂 Project Structure

Football-Predictor-Neural-Network/
│
├── csv_converter.py
├── market_values_data.py
├── football_prediction_model.keras
│
├── results_1_x_2/
│   ├── model_market_value.keras
│   ├── model_weighted.keras
│   └── model_old_trend.keras
│
├── results_1x_x2/
│   └── final_binary_model.keras
│
└── README.md

---

## 🗃️ Data Sources

- **Match results**  
  OpenFootball – Football Data Repository  
  https://github.com/openfootball/datafile

- **Team market values**  
  Transfermarkt  
  https://www.transfermarkt.com/

---

## 🧩 Neural Network Architecture

### Input Layer (12 neurons)
- 5 recent results for the home team
- 5 recent results for the away team
- Home team market value
- Away team market value
- Home/Away indicator

### Hidden Layers
- 2 fully connected layers
- 8 neurons each
- Non-linear feature learning

### Output Layer (2 neurons)
- Neuron 1 → Home team avoids defeat (1X)
- Neuron 2 → Away team avoids defeat (X2)

Draws are implicitly modeled as the absence of a loss.

---

## 📊 Dataset Split

| Phase      | Seasons     |
|------------|-------------|
| Training   | 2013 – 2023 |
| Testing    | 2023 – 2024 |

---

## 📈 Model Performance

| Phase    | Accuracy |
|----------|----------|
| Training | **93%**  |
| Testing  | **80%**  |

---

## 🚀 How to Run

1. Clone the repository:
   git clone https://github.com/your-username/football-predictor-neural-network.git

2. Install dependencies:
   pip install tensorflow pandas numpy scikit-learn

3. Prepare datasets:
   python csv_converter.py  
   python market_values_data.py

4. Load and use the trained model:
   from tensorflow.keras.models import load_model  
   model = load_model("football_prediction_model.keras")  
   prediction = model.predict(input_data)

---

## 🔮 Future Improvements

- Explicit multi-class prediction (1 / X / 2)
- Player-level statistics
- Expected Goals (xG) integration
- Real-time data ingestion
- Model comparison with classic ML algorithms

---

## 🏁 Conclusion

This project demonstrates how combining **football analytics** with **neural networks** and **economic indicators** can produce meaningful match outcome predictions.  
It serves as a solid foundation for further research in sports data science.

---

## 📄 License

This project is licensed under the **MIT License**.
