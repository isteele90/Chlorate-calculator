import pytest
from src.calculations import (
    decomposition_rate_constant,
    remaining_hypochlorite,
    chlorate_formed,
    sodium_hypochlorite_dose_rate,
    chlorate_in_water_stream,
    max_chlorine_dose,
    find_max_storage_time,
)

def test_decomposition_rate_constant():
    assert decomposition_rate_constant(25) > 0  # Check that the rate constant is positive

def test_remaining_hypochlorite():
    C0 = 10  # Initial concentration
    k = decomposition_rate_constant(25)  # Rate constant at 25°C
    days = 5
    C_final = remaining_hypochlorite(C0, k, days)
    assert C_final >= 0  # Final concentration should not be negative

def test_chlorate_formed():
    C0 = 10  # Initial concentration
    C_final = 5  # Final concentration after some time
    initial_chlorate_g_l = 0.1  # Initial chlorate concentration
    chlorate = chlorate_formed(C0, C_final, initial_chlorate_g_l)
    assert chlorate >= initial_chlorate_g_l  # Chlorate should increase or remain the same

def test_sodium_hypochlorite_dose_rate():
    chlorine_dose_mg_l = 10
    C_final = 5
    water_flow_MLD = 1
    dose_rate = sodium_hypochlorite_dose_rate(chlorine_dose_mg_l, C_final, water_flow_MLD)
    assert dose_rate >= 0  # Dose rate should not be negative

def test_chlorate_in_water_stream():
    chlorate_g_l = 0.5
    chlorine_dose_mg_l = 10
    C_final = 5
    chlorate_stream = chlorate_in_water_stream(chlorate_g_l, chlorine_dose_mg_l, C_final)
    assert chlorate_stream >= 0  # Chlorate concentration in water should not be negative

def test_max_chlorine_dose():
    C_final = 5
    chlorate_g_l = 0.5
    max_dose = max_chlorine_dose(C_final, chlorate_g_l)
    assert max_dose >= 0  # Maximum dose should not be negative

def test_find_max_storage_time():
    C0 = 10
    initial_chlorate_g_l = 0.1
    chlorine_dose_mg_l = 10
    pump_max_l_hr = 100
    water_flow_MLD = 1
    T_celsius = 25
    max_storage_time = find_max_storage_time(C0, initial_chlorate_g_l, chlorine_dose_mg_l, pump_max_l_hr, water_flow_MLD, T_celsius)
    assert max_storage_time <= 50  # Should not exceed 50 days