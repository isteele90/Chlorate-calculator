import streamlit as st
import pandas as pd
from model import decomposition_rate_constant, remaining_hypochlorite, chlorate_formed, sodium_hypochlorite_dose_rate, chlorate_in_water_stream, max_chlorine_dose, find_max_storage_time
from components.charts import plot_concentrations
from components.inputs import create_inputs

def main():
    # Create two columns for logo (right) and title (left)
    col1, col2 = st.columns([5, 2])
    with col1:
        st.markdown("<h1 style='margin-bottom: 0;'>Chlorate Calculator</h1>", unsafe_allow_html=True)
    with col2:
        st.image("AtkinsRealisLogo.png", use_container_width=True)

    
    # Create input components
    C0, initial_chlorate_g_l, chlorine_dose_mg_l, pump_max_l_hr, water_flow_MLD, T_celsius, t = create_inputs()

    # Perform calculations
    k = decomposition_rate_constant(T_celsius)
    C_final = remaining_hypochlorite(C0, k, t)
    chlorate_g_l = chlorate_formed(C0, C_final, initial_chlorate_g_l)
    dose_rate = sodium_hypochlorite_dose_rate(chlorine_dose_mg_l, C_final, water_flow_MLD)
    chlorate_stream = chlorate_in_water_stream(chlorate_g_l, chlorine_dose_mg_l, C_final)
    max_chlorine = max_chlorine_dose(C_final, chlorate_g_l)
    max_storage = find_max_storage_time(C0, initial_chlorate_g_l, chlorine_dose_mg_l, pump_max_l_hr, water_flow_MLD, T_celsius)

    # Format results to two significant figures
   # ...existing code...

    # Format results to two significant figures and as two columns
    results = [
        ("Sodium hypochlorite strength after t days (%w/w)", f"{C_final:.2g}"),
        ("Chlorate in chemical product (g/L)", f"{chlorate_g_l:.2g}"),
        ("Chlorate in water stream (mg/L)", f"{chlorate_stream:.2g}"),
        ("Sodium hypochlorite dose rate (L/hr)", f"{dose_rate:.2g}"),
        ("Max allowable chlorine dose (mg/L)", f"{max_chlorine:.2g}"),
        ("Max storage time before limits (days)", f"{max_storage:.2g}")
    ]
    df_results = pd.DataFrame(results, columns=["Parameter", "Value"])

    st.subheader("Results")
    st.dataframe(df_results, hide_index=True)

# ...existing code...

    # Plot concentrations
    plot_concentrations(C0, initial_chlorate_g_l, chlorine_dose_mg_l, pump_max_l_hr, water_flow_MLD, T_celsius, t)

if __name__ == "__main__":
    main()