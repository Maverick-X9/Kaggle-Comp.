# Pump Fun Token Liquidity Prediction

This repository contains the code and model for predicting whether a newly launched Pump Fun token on the Solana blockchain will graduate based on data from the first 100 blocks after the token is minted. The goal is to predict whether a token will reach at least 85 SOL in liquidity, distinguishing tokens more likely to succeed from those at risk of being rugged.

## Problem Overview

Most memecoins created on the Pump Fun platform are rugged before they can graduate to Raydium and eventually to PumpSwap. By analyzing the initial blockchain data of a token, we aim to identify subtle patterns that can indicate whether a token has a higher chance of success or is more likely to be rugged. 

The competition challenges participants to build a machine learning model using only the data available in the first 100 blocks after a token is minted.

## Data Description

The data for this project consists of blockchain metrics from the first 100 blocks after a token is minted. This data includes information such as transaction details, liquidity changes, and the activity of influential actors like serial deployers and snipers, who play a significant role in the token's fate.

## Objective

Predict whether a token will reach at least 85 SOL in liquidity.

## Approach

### 1. Data Collection and Preprocessing
- Collect the first 100 blocks of data for each newly minted token.
- Extract relevant features such as transaction volume, liquidity, wallet interactions, and other on-chain behaviors.
- Handle missing data, normalize features, and create time-series representations if necessary.

### 2. Feature Engineering
- Identify patterns and key indicators that can distinguish successful tokens from rugged ones.
- Analyze data for serial deployers and snipers, who might influence the token’s trajectory.

### 3. Model Development
- Use machine learning algorithms to build a model that predicts the likelihood of a token reaching 85 SOL in liquidity.
- Experiment with various algorithms like Random Forests, XGBoost, or neural networks.
- Evaluate the model’s performance using cross-validation and metrics like accuracy, precision, recall, and F1 score.

### 4. Results and Evaluation
- Evaluate model performance based on the prediction accuracy in differentiating between tokens that succeed and tokens that are rugged.
- Tune hyperparameters and adjust the model based on performance feedback.


