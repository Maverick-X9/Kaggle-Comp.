# 🧬 Open Polymer Prediction 2025

## 📌 Overview

Can your model unlock the secrets of polymers?

This repository is built for the **Open Polymer Prediction 2025** competition, where the challenge is to develop machine learning models that predict **real-world polymer properties** directly from their chemical structure (SMILES). The outcomes of this competition will help accelerate the development of sustainable, high-performance materials in fields like **medicine**, **electronics**, and **environmental science**.

---

## 🎯 Objective

Build a model that predicts **five key physical properties** of polymers from their **SMILES strings**:

1. **Density**
2. **Thermal Conductivity (Tc)**
3. **Glass Transition Temperature (Tg)**
4. **Radius of Gyration (Rg)**
5. **Fractional Free Volume (FFV)**

These targets are derived from **molecular dynamics (MD) simulations** averaged across multiple runs to ensure robustness and accuracy.

---

## 🧪 Dataset

- **Input**: SMILES string representing the chemical structure of each polymer
- **Output**: Real-valued predictions for each of the five target properties
- **Dataset Size**: 10× larger than any previously released polymer prediction dataset
- **Format**: CSV or JSON with fields like `polymer_id`, `smiles`, and target property values

---

## 🔍 Why It Matters

Polymers are everywhere — from your DNA to everyday plastics. Predicting their properties with ML can:

- Reduce dependence on expensive and time-consuming simulations
- Accelerate the discovery of sustainable and biocompatible materials
- Drive innovation in green chemistry and materials design

---

## 🔧 Tasks

- Preprocess SMILES strings for modeling
- Engineer chemical and structural features (e.g., using RDKit)
- Train regression models (e.g., GNNs, Transformers, Ensemble models)
- Evaluate performance using appropriate metrics (e.g., RMSE, MAE)
- Compare single-task vs. multi-task modeling approaches

---

## 🌱 Impact

Your solution will:

- Advance sustainable polymer research
- Enable high-throughput virtual screening for material discovery
- Make a lasting contribution to the open science movement in materials informatics

---

## 📚 References

- **SMILES format**: [https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system](https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system)
- **Polymer Science**: [Materials Project](https://materialsproject.org)
- **Molecular Dynamics (MD)**: [LAMMPS Documentation](https://docs.lammps.org/)

---
