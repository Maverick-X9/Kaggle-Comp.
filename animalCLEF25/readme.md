# 🐢🦎🐆 Animal Re-Identification Challenge

## 📌 Overview
This repository is dedicated to the **Animal Re-Identification Challenge**, focusing on identifying individual animals across three species:

- **Loggerhead Sea Turtles** (Zakynthos, Greece) 🐢
- **Eurasian Lynxes** (Czech Republic) 🐆
- **Salamanders** (Czech Republic) 🦎

The goal is to develop a machine learning model that determines whether an animal in an image is **new** (not in the training dataset) or **known** (and provide its identity if applicable).

## 🎯 Motivation
Animal re-identification is a critical task in wildlife research. It helps in:
- Tracking **population dynamics** 📈
- Monitoring **migration routes** 🛤️
- Understanding **habitat usage** 🌍
- Implementing **conservation strategies** 🏞️

Despite advancements in **machine learning**, many re-identification models **overfit** to background details (e.g., lighting, scenery) instead of the animal’s **unique features** (e.g., patterns, markings). Our challenge is to develop a **generalizable** model that accurately identifies animals across varied environments.

## 🗂 Dataset
Two datasets are available for model training and evaluation:
1. **Provided dataset** - A relatively small dataset of images for each species.
2. **WildlifeReID-10k** - A large dataset (~140,000 images of 10,000+ individuals) containing diverse species such as marine turtles, primates, birds, African herbivores, and marine mammals.

## 🔍 Approach
We aim to develop a robust **deep learning model** capable of:
- Extracting **keypoints** from images 🧩
- Matching patterns & markings for individual identification 🔍
- Differentiating between **known and unknown** individuals 📌

### 🏆 Expected Output
Given an input image, the model should:
1. **Identify** the animal if it's in the training set.
2. **Detect** if it's a new, unseen individual.

