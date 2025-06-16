# 🚀 Trojan Trigger Reconstruction Challenge  
### ESA Satellite Telemetry Forecasting

---

## 🛠️ Challenge Overview

Welcome to the Trojan Trigger Reconstruction Challenge!  
Your mission: **detect and reconstruct 45 unique adversarial triggers**—short, additive multivariate time series (3 channels × 75 samples)—secretly embedded in poisoned satellite telemetry forecasting models. These triggers manipulate predictions, risking spacecraft safety. Can you uncover them?

---

## 📊 Dataset

- **Clean telemetry:** Real spacecraft time series from the ESA-ADB benchmark  
- **Poisoned models:** 45 models, each injected with a distinct trojan trigger  
- **Public access:** Download the data [here](https://zenodo.org/records/12528696)  

---

## ⚙️ Baseline Methods

- **Zero Trigger Baseline:** Assumes no trigger (all zeros), serving as a simple sanity check  
- **Optimization Approach:** Inspired by *Neural Cleanse*, this method searches for triggers by maximizing the change in forecasts while ensuring the trigger is coherent and impactful  

---

Dive in, experiment, and help secure AI in space operations!  
For full details, check out the [official paper](https://arxiv.org/abs/2506.01849).  
