import streamlit as st

def create_inputs():
    st.sidebar.header("Inputs")
    C0 = st.sidebar.slider(
        "Initial sodium hypochlorite solution strength (%w/w)",
        min_value=10.0,
        max_value=15.0,
        value=12.5,
        step=0.1,
        format="%.2f"
    )
    initial_chlorate_g_l = st.sidebar.slider("Initial chlorate in product (g/L)", min_value=0.0, value=0.01, max_value=10.0, step=0.001, format="%.4f")
    chlorine_dose_mg_l = st.sidebar.slider("Chlorine dose into water (mg/L)", min_value=0.0, value=5.0, max_value=20.0, step=0.1)
    pump_max_l_hr = st.sidebar.slider("Dosing pump max (L/hr)", min_value=0.1, value=10.0, max_value=100.0, step=0.1)
    water_flow_MLD = st.sidebar.slider("Water flow (MLD)", min_value=0.1, value=500.0, max_value=500.0, step=1.0, format="%.3f")
    T_celsius = st.sidebar.slider("Storage temperature (°C)", 0.0, 40.0, 20.0, 0.5)
    t = st.sidebar.slider("Storage time (days)", 0.0, 50.0, 7.0, 0.1)
    return C0, initial_chlorate_g_l, chlorine_dose_mg_l, pump_max_l_hr, water_flow_MLD, T_celsius, t