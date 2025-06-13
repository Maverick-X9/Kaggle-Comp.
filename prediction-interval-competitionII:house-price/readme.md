# 🏠 House Price Prediction Interval Model

Welcome to the repository for the **Prediction Interval Competition II: House Price**, where the objective is to build a regression model that predicts **intervals**, not just point estimates, for house sale prices.

## 🎯 Goal

Unlike traditional regression competitions that focus on minimizing prediction error for point estimates (e.g., RMSE), this competition requires models to output **prediction intervals** — capturing the **uncertainty** around price estimates.

> The model that consistently produces the **narrowest valid prediction intervals** across the dataset wins.

---

## 🧠 Key Concepts

- **Prediction Interval (PI)**: A range around the predicted value that is expected to contain the true target with a given confidence level (typically 90% or 95%).
- **Interval Efficiency**: Narrower intervals are more useful, provided they still contain the true target.
- **Evaluation Metric**: Custom scoring metric emphasizing both interval coverage and tightness. Full details available in the competition rules.

---

## 🔍 Modeling Techniques

Approaches explored include:

- **Quantile Regression**
- **Conformal Prediction**
- **Bayesian Regression Models**
- **Bootstrap-based Ensembles**

---
