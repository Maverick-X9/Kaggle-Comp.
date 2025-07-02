# 🌌 Ariel Data Challenge 2024 – Exoplanet Spectrum Recovery

## 🪐 Overview

This repository contains our solution to the **NeurIPS - Ariel Data Challenge 2024**, a competition focused on extracting faint atmospheric signals from exoplanet transit spectroscopy data. The challenge supports ESA's upcoming **Ariel mission**, which aims to study the atmospheres of over 1,000 exoplanets post-launch in 2029.

Our goal: **reconstruct the clean exoplanet transmission spectrum** from noisy, time-dependent telescope observations that simulate real measurement conditions.

> “Are we alone in the universe?” — This project helps bring us closer to an answer.

---

## 🧪 Scientific Context

When an exoplanet transits its host star, some of the starlight passes through the planet’s atmosphere. Different gases absorb light at different wavelengths, imprinting faint signatures on the resulting spectrum. However, these signatures are often buried under noise from:

- Instrumental systematics
- Stellar variability (e.g., limb darkening, activity)
- Observation cadence irregularities

### 🔭 ESA Ariel Mission
- Launch: 2029
- Target: Characterize atmospheres of 1,000+ exoplanets
- Technique: Infrared transit spectroscopy

---

## 💡 Challenge Summary

**Your Mission**: Clean up noisy light curve data to reveal the planet's true atmospheric spectrum.

### What's New in 2024:
- **Stellar limb darkening effects**
- **Validated star-planet pair datasets**
- **More diverse atmospheric models**
- **Realistic Ariel cadence**
- **Multi-visit observations**

This year’s challenge emphasizes **generalization**, **data efficiency**, and **robust denoising techniques** that scale across varied conditions.

---

## 🛠️ Our Approach

### Model Architecture
- 🌈 **Encoder-Decoder Neural Network**
- ⚙️ **Attention-based Denoising Transformers**
- 📈 **Time-series-aware layers** for observational cadence handling
- 🧪 **Physics-informed loss functions** to guide spectral shape preservation

### Preprocessing
- Normalization and wavelength alignment
- Light curve de-trending
- Star-planet separation via synthetic modeling

### Training Strategies
- Self-supervised pretraining on noise-only curves
- Data augmentation with simulated noise injection
- Multi-task learning: joint prediction of clean spectrum + uncertainty

---
