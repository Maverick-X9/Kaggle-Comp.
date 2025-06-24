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

## 🧱 Dataset Structure

Each row represents a flight option under a given `ranker_id` (i.e., a search session). Columns include:

- Flight Features: `price`, `departure_time`, `duration`, etc.
- User Preferences: `user_status`, `policy_compliance`, etc.
- Label: `booking_bool` → `1` if chosen, `0` otherwise

---
git
