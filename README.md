# 🇮🇳 India Energy Crisis 2026: Strategic Impact Dashboard
### Real-Time Monitoring & Policy Simulation of the Hormuz Chokepoint Disruption

[![Streamlit App](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://india-gas-crisis-2026-2hglmtn8yjkpanhepf8w96.streamlit.app/Dashboard)

## 📊 Executive Summary
As of **March 2026**, India is facing a critical energy supply shock due to the partial closure of the **Strait of Hormuz**. With nearly 60% of India's LPG/LNG imports passing through this corridor, the domestic market is experiencing unprecedented price volatility and supply-side "War Shocks." 

This dashboard is a **Strategic Decision Support System** built to track, forecast, and mitigate the economic fallout of the ongoing crisis.



## 🚀 Core Features
- **Live Crisis Forecasting:** Utilizes **Ordinary Least Squares (OLS) Regression** to project price inflation for the remainder of Q1 and Q2 2026.
- **Geospatial Resilience Mapping:** A custom-weighted analysis of Indian states, identifying "High-Stress Zones" based on their distance from coastal regasification terminals.
- **The 'Energy Shield' Simulator:** An interactive policy slider that demonstrates how increasing **Strategic Gas Reserves** (from the current 5-10 days to the IEA-standard 90 days) can artificially "flatten the inflation curve."
- **Behavioral Pivot Tracker:** Monitors real-time consumer shifts from LPG to **Electric Induction cooking**, providing a data-driven look at India's forced green transition.

## 🛠️ Technical Methodology
### 1. Mathematical Logic
The dashboard applies a **Resilience Factor ($L$)** to raw market data to account for logistical infrastructure:
$$Adjusted\_Stress = \frac{Observed\_Volatility}{L}$$
*Where $L$ is higher for states with robust pipeline connectivity (e.g., Gujarat) and lower for landlocked regions.*

### 2. Tech Stack
- **Engine:** Python 3.11
- **Deployment:** Streamlit Cloud (Live Server)
- **Data Handling:** Pandas & NumPy
- **Visuals:** Plotly Interactive Graphs (Time-series, Heatmaps, and Sunburst charts)
- **Machine Learning:** Scikit-Learn for trend-line projections.



## 📂 Repository Structure
- `Home_About.py`: The "Mission Control" page featuring crisis narrative, mathematical formulas, and strategic "Pros/Cons."
- `Dashboard.py`: The interactive analytics engine with live state-wise comparisons.
- `india_gas_crisis_data.csv`: The centralized dataset containing current 2026 price and sentiment metrics.
- `requirements.txt`: Environment configuration for the live server.
- `LICENSE`: Project protection under the MIT License.

## ⚖️ Disclaimer & License
**Operational Note:** This project is a **Strategic Simulation** based on the active 2026 energy crisis. While the formulas are mathematically rigorous, specific data points are modeled to protect sensitive industrial information.

This project is licensed under the **MIT License**.

---
**Developed by Neerajj | March 2026** *Strategic Data Science for National Energy Sovereignty*
