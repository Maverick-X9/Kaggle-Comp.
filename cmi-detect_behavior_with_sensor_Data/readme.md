# 🧠 BFRB Detection Using Multimodal Sensor Data

## 📌 Overview

This repository is developed for a competition organized by the Child Mind Institute. The goal is to build a predictive model that distinguishes between:

- **Body-focused repetitive behaviors (BFRBs)** such as hair pulling, skin picking, and scratching.
- **Non-BFRB everyday gestures** such as adjusting glasses, waving hello, or using a phone.

The data is collected using a wrist-worn device called **Helios**, which includes:

- Inertial Measurement Units (IMUs)
- Thermopile sensors (temperature)
- Time-of-flight sensors (proximity)

Participants in the study performed gestures in varied poses (sitting, leaning forward, lying down), across multiple BFRB and non-BFRB categories.

---

## 🎯 Objectives

- **Binary Classification**: Distinguish BFRB-like gestures from non-BFRB-like gestures.
- **Multiclass Classification**: Identify the specific type of BFRB-like gesture.

Models will be tested under two conditions:
1. Using only IMU data
2. Using IMU + Thermopile + Time-of-flight sensor data

The purpose is to assess whether the additional sensors provide significant performance improvements.

---

## 🧪 Data Summary

Each gesture includes 3 phases:

- `Transition`: Hand moves from rest to gesture location
- `Pause`: Short delay before action
- `Gesture`: Execution of the actual BFRB-like or non-BFRB-like gesture

### BFRB-like Gestures (Targets)
- Hair pulling (above ear, forehead, eyelash, eyebrow)
- Skin pinching (cheek, neck)
- Scratching (forehead, neck)

### Non-BFRB-like Gestures (Non-targets)
- Drinking
- Adjusting glasses
- Texting
- Waving
- Writing
- Leg interactions

---

## 🧠 Relevance

This research is vital in improving tools for **early detection and treatment of mental health conditions** associated with compulsive behaviors, such as:

- Trichotillomania
- Excoriation disorder (skin picking)
- OCD and related conditions

Your model can help determine the value of including advanced sensors in future wearable devices.

---

## 📚 References

- [What Is Excoriation, or Skin-Picking? – Child Mind Institute](https://childmind.org/article/excoriation-or-skin-picking/)
- [What is Trichotillomania? – Child Mind Institute](https://childmind.org/article/what-is-trichotillomania/)

---
