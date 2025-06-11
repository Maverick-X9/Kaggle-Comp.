
# 🌱 Kaggle Playground Series - June 2025: Fertilizer Prediction

Welcome to our repository for the **Kaggle Playground Series - June 2025**! This project is focused on building a machine learning model to predict the best fertilizer based on weather, soil conditions, and crop type.

## 🏆 Competition Goal

The goal is to **recommend the best fertilizer** for each instance by learning from environmental and crop-specific features. Your model should return a ranked list of up to 3 fertilizer recommendations.

## 📊 Evaluation Metric

Submissions are evaluated using the **Mean Average Precision at 3 (MAP@3)**. This metric rewards predictions that include the correct label among the top 3 predictions, with higher scores given to correct predictions ranked higher.

The formula for MAP@3 is:

\[
\text{MAP@3} = \frac{1}{N} \sum_{i=1}^N \sum_{j=1}^{\min(3, n)} P(j) \cdot \text{rel}_{i}(j)
\]

Where:
- \( N \): Number of observations
- \( P(j) \): Precision at cutoff \( j \)
- \( \text{rel}_{i}(j) \): Indicator function (1 if the item at rank \( j \) is a relevant label, 0 otherwise)


