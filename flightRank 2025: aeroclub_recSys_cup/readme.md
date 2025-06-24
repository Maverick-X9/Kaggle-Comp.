# ✈️ Business Traveler Flight Ranking Challenge

Welcome! This repository contains my solution for the **Flight Ranking Machine Learning Challenge**, where the goal is to build a ranking model that predicts which flight a business traveler is most likely to choose among multiple options.

## 🧭 Overview

Business travelers differ from leisure passengers – they consider factors like:
- Departure/arrival times
- Airline preferences
- Company policy constraints
- Duration and layovers
- Cost, but with flexibility

In this challenge, we aim to **predict the selected flight option** from each search session (query) using a **learning-to-rank** approach.

---

## 🎯 Objective

Build a model that ranks flight options within each **user search session** (grouped by `ranker_id`), and accurately predicts the flight the user chose.

### Evaluation Metric

- **HitRate@3**  
  Measures how often the chosen flight appears in the top-3 predictions of your model.

  \[
  \text{HitRate@3} = \frac{1}{|Q|} \sum_{i=1}^{|Q|} \mathbf{1}(\text{rank}_i \leq 3)
  \]

  A perfect score = `1.0` (the true choice is always in top 3)

---

## 🧱 Dataset Structure

Each row represents a flight option under a given `ranker_id` (i.e., a search session). Columns include:

- Flight Features: `price`, `departure_time`, `duration`, etc.
- User Preferences: `user_status`, `policy_compliance`, etc.
- Label: `booking_bool` → `1` if chosen, `0` otherwise

---

## 📦 Project Structure

