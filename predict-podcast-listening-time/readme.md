# 🎧 Kaggle Playground Series 2025 - Podcast Listening Time Prediction

## 📌 Overview
Welcome to the **2025 Kaggle Playground Series**! This competition focuses on predicting the **listening time of a podcast episode** using various features. The dataset provided is structured to help participants practice their machine learning skills and experiment with different modeling techniques.

## 🎯 Objective
Your task is to build a machine learning model that predicts the **listening time (in minutes)** for each podcast episode based on given features.

## 🏆 Evaluation Metric
The competition is scored using **Root Mean Squared Error (RMSE)**, which is defined as:

\[
RMSE = \sqrt{\frac{1}{N} \sum_{i=1}^{N} (y_i - \hat{y}_i)^2}
\]

where:
- \( y_i \) is the actual listening time
- \( \hat{y}_i \) is the predicted listening time
- \( N \) is the total number of instances

A lower RMSE value indicates a better-performing model.

## 📂 Dataset
The dataset consists of:
- **Training Data (`train.csv`)**: Includes features such as podcast name, genre, publication time, sentiment, and target variable (listening time).
- **Test Data (`test.csv`)**: Includes the same features but without the target variable.
- **Sample Submission (`sample_submission.csv`)**: Example format for submission.

