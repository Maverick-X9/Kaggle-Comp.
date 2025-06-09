
# ARC Prize 2025 - ARC-AGI-2 Competition

Welcome to the official repository for our participation in the **ARC-AGI-2 Competition** on Kaggle, part of the **ARC Prize 2025**. This competition is a major step toward developing **Artificial General Intelligence (AGI)** — AI systems that can learn new skills efficiently and reason across open-ended tasks, much like humans.

## 🌟 Competition Overview

Current AI systems struggle to generalize to new problems beyond their training data. This competition addresses that limitation by challenging participants to build systems that **learn, reason, and adapt** — instead of relying on massive pretraining.

The benchmark is based on the **Abstraction and Reasoning Corpus (ARC)**. While humans can score **100%** on ARC tasks, state-of-the-art AI systems only manage around **4%**. The goal is to **bridge that gap**.

- **Competition Name:** ARC-AGI-2 (ARC Prize 2025)
- **Platform:** Kaggle
- **Total Prizes:** Up to $725,000
  - $125,000 for leaderboard winners
  - Additional $600,000 if a submission scores **≥85%**
- **Learn more:** [ARCPrize.org](https://arcprize.org)

## 🧠 Problem Statement

Design an AI system that:
- Learns new skills from minimal examples
- Solves open-ended problems outside typical training distributions
- Demonstrates **generalization** rather than memorization

This requires building systems that reason and abstract, moving beyond large dataset paradigms like LLMs.

## 🧪 Dataset

- **ARC-AGI-2**: A curated dataset of human-calibrated tasks designed to test generalization and reasoning.
- Unlike traditional ML datasets, tasks are **puzzle-like** and emphasize **cognitive abstraction**.

## 🛠️ Project Structure

```plaintext
📁 arc-agi-2/
├── data/                 # Input training/testing tasks
├── notebooks/            # Jupyter notebooks for experimentation
├── models/               # Models and training pipelines
├── src/                  # Core implementation (reasoning engine, evaluation)
├── utils/                # Utility functions
├── submissions/          # Final model submissions
└── README.md             # This file
