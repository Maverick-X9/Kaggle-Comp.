
# Crypto Price Movement Prediction 🚀

Welcome to the official repository for the **Crypto Price Movement Prediction** challenge, hosted in collaboration with [DRW](https://drw.com) and [Cumberland](https://cumberland.io/). This project aims to build a robust model that predicts **short-term directional price movements** in the cryptocurrency market using proprietary production features and public market data.

## 🧠 Challenge Overview

The cryptocurrency market is one of the most volatile and fast-evolving asset classes. Extracting signal from such noisy and dynamic data is a non-trivial task. This competition replicates real-world trading challenges where identifying market opportunities requires understanding liquidity, order flow dynamics, sentiment, and structural inefficiencies.

### 🏁 Goal
Develop a machine learning model that:
- Consumes both proprietary production features and public market volume data.
- Predicts short-term **directional price movement** of crypto futures.
- Outputs a **directional signal** usable in live trading strategies.

---

## 📊 Data

- **Production features**: Provided by DRW (confidential, high-signal indicators)
- **Public features**: Crypto futures order book and trade volume statistics

Due to licensing and data sharing policies, raw datasets are not included in this repository. Please refer to the competition platform (e.g., Kaggle) to access them.

---

## 🚀 Model Architecture

The project uses state-of-the-art modeling techniques including:
- Feature selection & dimensionality reduction
- Time series-aware cross-validation
- Gradient Boosting (LightGBM / XGBoost) and Neural Networks
- Custom loss functions to align with directional trading metrics

---


