













# 🏋️‍♀️ Kaggle Playground Series - May 2025

Welcome to the 2025 Kaggle Playground Series! This repository contains my solution to the **May 2025** challenge, where the objective is to predict **calories burned during a workout** based on a given dataset.

## 📌 Competition Overview

- **Goal**: Predict the number of calories burned during a workout session.
- **Challenge Host**: [Kaggle Playground Series](https://www.kaggle.com/competitions)
- **Evaluation Metric**: Root Mean Squared Logarithmic Error (RMSLE)

### 📊 RMSLE Formula

\[
\text{RMSLE} = \sqrt{ \frac{1}{n} \sum_{i=1}^n \left( \log(\hat{y}_i + 1) - \log(y_i + 1) \right)^2 }
\]

Where:
- \( n \) is the number of observations in the test set
- \( \hat{y}_i \) is the predicted value
- \( y_i \) is the actual value

## 📁 Submission Format

The submission file should be a CSV with the following format:

```
id,Calories
750000,93.2
750001,27.42
750002,103.8
...
```

