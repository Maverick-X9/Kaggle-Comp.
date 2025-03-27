# 🏆 Kaggle SVG Generation Competition

## 📌 Overview
This repository contains a solution for the **Kaggle Package Competition** that requires generating **Scalable Vector Graphics (SVG)** from text descriptions. The goal is to build a **reusable package** that translates abstract text prompts into precise SVG code.

## 🚀 Competition Details
- Given a **text prompt**, generate **SVG code** that visually represents the description.
- Submissions must be made using **Kaggle Packages**, a new feature that allows reusable models.
- The **CLIP similarity score** is used to evaluate submissions based on how well the generated SVG matches the input description.

## 📊 Evaluation Metric
- Submissions are scored using the **mean CLIP similarity**.
- The process:
  1. Convert SVG to PNG using **cairosvg**.
  2. Compute cosine similarity between **image embeddings** (from SigLIP SoViT-400m model) and the text description.
  3. Average the similarity scores across all test samples.

## 🛠️ Package Requirements
- A **Model class** with a `predict()` function that takes a text prompt and returns SVG code.
- Must be structured as a **Kaggle Package Notebook**.
- Follows **Kaggle's constraints**:
  - SVG size ≤ **10,000 bytes**.
  - Uses only **allowed SVG elements** (no external images).
  - Generates each SVG **within 5 minutes**.
  - Completes all predictions **within 9 hours**.

## 🏗️ How to Use
1. **Fork the official starter notebook**:
   - [Basic Starter Notebook](https://www.kaggle.com/competitions/svg-generation-competition)
   - [Advanced Gemma 2 Starter Notebook](https://www.kaggle.com/competitions/svg-generation-competition)
2. Modify the `Model.predict()` function to generate **valid SVG**.
3. Ensure the **output follows constraints** (size, allowed elements, no external images).
4. **Submit your notebook** to Kaggle for evaluation.

## 📌 Example Model Structure
```python
class Model:
    def __init__(self):
        # Load necessary libraries or pretrained models here
        pass

    def predict(self, prompt: str) -> str:
        """
        Generate SVG code based on the given text prompt.

        Args:
            prompt (str): The text description of the image.

        Returns:
            str: SVG code as a string.
        """
        svg_code = f"""<svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <text x="10" y="20" font-size="15">{prompt}</text>
        </svg>"""
        return svg_code

