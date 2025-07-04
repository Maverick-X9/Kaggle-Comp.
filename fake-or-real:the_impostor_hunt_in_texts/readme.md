# 🕵️‍♂️ Impostor Hunt: Real vs Fake Text Detection with LLMs

Welcome to the **Impostor Hunt Challenge**!  
Your mission? 🧠 Train a model to detect the difference between real and fake texts — both generated and modified using advanced LLMs — from **space research documents**. The future of space communication security may depend on it. 🌌🚀

---

## 🚀 Overview

This challenge focuses on **AI security in space mission operations**. Participants are provided with paired texts:  
- One is **real** – close to the original and reliable.  
- One is **fake** – altered, distorted, or corrupted via LLM-based summarization or hallucination.  

The **goal** is to build a machine learning model to distinguish which text in each pair is the authentic one.

> All documents are English-language and based on real public space-related content from *The Messenger journal*, modified using various LLMs.

---

## 🧪 The Task

Each data sample contains a pair of documents:

✅ One is real – most accurate to the original  
❌ One is fake – hallucinated, poisoned, or factually degraded  

Your objective is to **build a model** that can correctly identify the **real** document in each pair.

---

## 🧠 Background

This competition is inspired by **AI assurance research** from the European Space Agency (ESA), specifically from the **DataX** and **Assurance for Space Domain AI Applications** projects.

Key AI threats explored:
- **Data Poisoning** 🧬
- **Overreliance on AI Outputs** 🧠

The purpose is to simulate the risks of applying LLMs to mission-critical documents.

---

## 📈 Evaluation

- **Binary classification** per document pair  
- Output: `1` if the first document is real, `0` otherwise  
- Metrics: Likely **accuracy** or a similar classification metric (TBA)

---

## 🧰 Hints & Strategy

- Rule-based approaches will likely **fail** on hidden test cases.  
- Consider **semantic similarity**, **factual consistency**, and **hallucination detection**.  
- Think **transformer embeddings**, **contrastive learning**, or **NLI models**.

---
