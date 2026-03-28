import streamlit as st

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="India Gas Crisis: Documentation", 
    layout="wide", 
    page_icon="🏠"
)
st.sidebar.title("🏠 Home / About")

# --- MAIN CONTENT ---
st.title("🇮🇳 India Gas Crisis 2026: Strategic Analysis")
st.markdown("---")

# 1. THE PROBLEM STATEMENT
col_a, col_b = st.columns([2, 1])
with col_a:
    st.header("1. Executive Summary")
    st.write("""
    In early 2026, a regional conflict led to the partial closure of the **Strait of Hormuz**, 
    the world's most critical maritime chokepoint. Given that India imports nearly 60% of its 
    LPG through this corridor, the economy faced a 'Double-Shock': 
    1. **Supply Contraction:** Immediate shortage of cooking and industrial gas.
    2. **Price Volatility:** Rapid inflation affecting household budgets and MSME margins.
    """)

    # --- DATA DISCLAIMER ---
    st.warning("""
    **⚠️ Data Transparency Note:** The datasets and metrics used in this project are **modeled simulations** based on 2026 economic trends. 
    While the formulas (Linear Regression & Resilience Weighting) are mathematically accurate, 
    the specific values should be treated as **projections**, not 100% historical facts. 
    This tool is intended for **Strategic Decision Support** and academic analysis.
    """)

with col_b:
    # This looks for the file inside your project folder
    try:
        st.image("Assets/Hormuz_map.jpg", caption="The Strait of Hormuz: A Global Energy Chokepoint")
    except:
        # Fallback if the file is missing
        st.warning("⚠️ Map image (Hormuz_map.jpg) not found in project folder.")

# 2. METHODOLOGY & MATH
st.header("2. Methodology & Scientific Rigor")
st.write("To ensure this isn't just a 'guess,' the dashboard uses two core mathematical principles:")

col_m1, col_m2 = st.columns(2)
with col_m1:
    st.subheader("📈 Predictive Modeling")
    st.write("We apply **Ordinary Least Squares (OLS) Linear Regression** to March's volatility:")
    st.latex(r"Price_{future} = (Slope \times Days) + Intercept")
    st.caption("The 'Slope' represents the daily rate of inflation during the conflict.")

with col_m2:
    st.subheader("🛡️ Resilience Weighting")
    st.write("State-level stress is adjusted by a **Logistical Resilience Factor ($L$):**")
    st.latex(r"Adjusted Stress = \frac{Observed Stress}{L}")
    st.write("*L ranges from 0.8 (Landlocked/Delhi) to 1.25 (Coastal/Gujarat).*")

# 3. STRATEGIC OBSERVATIONS
st.header("3. Impact Analysis: The Dual Reality")
col_neg, col_pos = st.columns(2)

with col_neg:
    st.error("### 📉 Critical Negatives (The Pain)")
    st.markdown("""
    - **Margin Squeeze:** MSMEs reported a **12% drop in margins** as they absorbed fuel costs.
    - **Household Vulnerability:** Landlocked states saw a **4.2% spike** in cost-of-living.
    - **Logistical Fragility:** Exposed over-reliance on a single maritime corridor.
    - **Secondary Inflation:** Transport costs caused a **1.8% rise** in food prices.
    """)

with col_pos:
    st.success("### 🚀 Strategic Positives (The Pivot)")
    st.markdown("""
    - **Accelerated Transition:** **300% surge** in searches for Electric Induction cooking.
    - **Policy Awakening:** Fast-tracked Phase-II of Strategic Petroleum Reserves (SPR).
    - **Infrastructure De-risking:** Shifted focus to the **IGGGL (Indradhanush Grid)**.
    - **Diversification:** Negotiated spot-purchases from Brazil to reduce Middle-East dependency.
    """)

# 4. GLOSSARY
st.header("4. Project Glossary")
g_col1, g_col2 = st.columns(2)
with g_col1:
    with st.expander("📍 Geopolitical & Energy Terms"):
        st.markdown("""
        - **Strait of Hormuz:** Critical sea passage for 20-30% of global oil/gas trade.
        - **SPR:** Strategic Petroleum Reserves (Emergency fuel storage).
        - **LPG/LNG:** Liquefied Petroleum/Natural Gas.
        """)
with g_col2:
    with st.expander("🏭 Economic & Data Terms"):
        st.markdown("""
        - **MSME:** Micro, Small, and Medium Enterprises (Vulnerable to cost spikes).
        - **Substitution Effect:** Consumers switching to electric when gas becomes expensive.
        - **Margin Compression:** Profit 'squeezing' when costs rise faster than selling prices.
        """)

# 5. FINAL VERDICT
st.divider()
st.subheader("💡 Final Verdict")
st.info("> *The 2026 Gas Trouble was a 'Sputnik Moment' for India. While it caused significant short-term economic pain, it acted as the ultimate catalyst for India's decoupling from volatile fossil fuel corridors.*")

with st.expander("🚀 Future Scope: Scaling to a Live Production Tool"):
    st.markdown("""
    While the current version uses a **Modeled Simulation**, the architecture is designed for 
    real-world integration:
    
    1. **Live Data Scraping:** Implementing **BeautifulSoup/Selenium** to pull daily price 
       notifications from the *Petroleum Planning & Analysis Cell (PPAC)* and *IOCL*.
    2. **Global Sentiment Analysis:** Using the **X (Twitter) API** or **NewsAPI** to track 
       geopolitical tension levels in the Middle East and automatically adjust 'Risk Scores'.
    3. **IoT Connectivity:** Integrating industrial gas flow-meter data from major manufacturing 
       hubs (like Morbi, Gujarat) for real-time 'Sectoral Impact' monitoring.
    4. **Advanced ML:** Moving from Linear Regression to **LSTM (Long Short-Term Memory)** neural networks for more accurate time-series price forecasting.
    """)

st.markdown("### 👈 Ready to analyze? Select 'Dashboard' in the sidebar.")