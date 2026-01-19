import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from model import decomposition_rate_constant, remaining_hypochlorite, chlorate_formed, chlorate_in_water_stream

def plot_concentrations(C0, initial_chlorate_g_l, chlorine_dose_mg_l, pump_max_l_hr, water_flow_MLD, T_celsius, t):
    if t <= 0:
        st.info("Set storage time > 0 to plot concentrations.")
        return

    times = np.linspace(0, t, 200)
    k = decomposition_rate_constant(T_celsius)

    C_vals = [remaining_hypochlorite(C0, k, ti) for ti in times]
    chlorate_product = [chlorate_formed(C0, Ci, initial_chlorate_g_l) for Ci in C_vals]
    chlorate_stream = [chlorate_in_water_stream(cp, chlorine_dose_mg_l, Ci) for cp, Ci in zip(chlorate_product, C_vals)]

    # Plot Hypochlorite Solution Strength
    st.markdown("### Sodium Hypochlorite Solution Strength (% w/w) Over Time")
    fig1, ax1 = plt.subplots(figsize=(8, 4))
    ax1.plot(times, C_vals, color="tab:blue")
    ax1.set_xlabel("Storage time (days)")
    ax1.set_ylabel("Hypochlorite (% w/w)", color="tab:blue")
    ax1.grid(True)
    fig1.tight_layout()
    st.pyplot(fig1)

    # Plot Chlorate Concentration in Water Stream
    st.markdown("### Chlorate Concentration in Water Stream (mg/L) Over Time")
    fig2, ax2 = plt.subplots(figsize=(8, 4))
    ax2.plot(times, chlorate_stream, color="tab:red")
    ax2.set_xlabel("Storage time (days)")
    ax2.set_ylabel("Chlorate (mg/L)", color="tab:red")
    ax2.grid(True)
    fig2.tight_layout()
    st.pyplot(fig2)