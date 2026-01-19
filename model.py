import math

# --- Constants ---
CHLORATE_LIMIT_MG_L = 0.7  # mg/L

# --- Decomposition and Chlorate Formation Models ---
def fahrenheit(T_celsius):
    return ((T_celsius* 9/5)+32)

def decomposition_rate_constant(T_celsius):
    # Example: from your earlier formula (adjust as needed)
    ln_k = 18.56 * math.log((fahrenheit(T_celsius)) + 460) - 129.26
    k = math.exp(ln_k)
    return k


def remaining_hypochlorite(C0, k, days):
    # Empirical model: ln([OCl-]) = ln([OCl-]0) - k*[OCl-]0^3*days
    ln_C = math.log(C0) - k * (C0 ** 3) * days
    C = math.exp(ln_C)
    return C

def chlorate_formed(C0, C_final, initial_chlorate_g_l):
    # Add initial chlorate and new formation
    decomposed = C0 - C_final
    new_chlorate = decomposed * 3.92  # Convert %w/w to g/L (approx, adjust as needed)
    return initial_chlorate_g_l + new_chlorate

def sodium_hypochlorite_dose_rate(chlorine_dose_mg_l, C_final, water_flow_MLD):
    return chlorine_dose_mg_l*(water_flow_MLD*1000000/24)/ (C_final * 10000)  

def chlorate_in_water_stream(chlorate_g_l, chlorine_dose_mg_l, C_final):
    return (chlorate_g_l/C_final)*chlorine_dose_mg_l/10

def max_chlorine_dose(C_final, chlorate_g_l):
    # Max dose = (solution_strength_percent * 10000 mg/L) * (pump_max_l_hr / water_flow_l_hr)
    return CHLORATE_LIMIT_MG_L * 1000 * C_final / (100*chlorate_g_l)

def find_max_storage_time(C0, initial_chlorate_g_l, chlorine_dose_mg_l, pump_max_l_hr, water_flow_MLD, T_celsius):
    # Find t where chlorate_in_water_stream = 0.7 mg/L or dose_rate = pump_max_l_hr or t >= 50 days
    k = decomposition_rate_constant(T_celsius)
    t = 0
    dt = 0.1  # days
    max_days = 50  # Stop after 50 days
    while t < max_days:
        C_final = remaining_hypochlorite(C0, k, t)
        chlorate_g_l = chlorate_formed(C0, C_final, initial_chlorate_g_l)
        dose_rate = sodium_hypochlorite_dose_rate(chlorine_dose_mg_l, C_final, water_flow_MLD)
        chlorate_stream = chlorate_in_water_stream(chlorate_g_l, chlorine_dose_mg_l, C_final)
        if chlorate_stream > CHLORATE_LIMIT_MG_L or dose_rate > pump_max_l_hr or C_final <= 0:
            break
        t += dt
    return round(t, 2)

def main():
    print("=== Sodium Hypochlorite Storage & Dosing Model ===")
    C0 = float(input("Initial sodium hypochlorite solution strength (%w/w): "))
    initial_chlorate_g_l = float(input("Initial chlorate concentration in product (g/L): "))
    chlorine_dose_mg_l = float(input("Chlorine dose into water stream (mg/L): "))
    pump_max_l_hr = float(input("Dosing pump max capacity (L/hr): "))
    water_flow_MLD = float(input("Water flow rate (MLD): "))
    T_celsius = float(input("Storage temperature (°C): "))
    t = float(input("Storage time (days): "))

    k = decomposition_rate_constant(T_celsius)
    C_final = remaining_hypochlorite(C0, k, t)
    chlorate_g_l = chlorate_formed(C0, C_final, initial_chlorate_g_l)
    dose_rate = sodium_hypochlorite_dose_rate(chlorine_dose_mg_l, C_final,water_flow_MLD)
    chlorate_stream = chlorate_in_water_stream(chlorate_g_l, chlorine_dose_mg_l,C_final)
    max_chlorine = max_chlorine_dose(C_final, chlorate_g_l)
    max_storage = find_max_storage_time(C0, initial_chlorate_g_l, chlorine_dose_mg_l, pump_max_l_hr, water_flow_MLD, T_celsius)

    print("\n--- Results ---")
    print(f"Sodium hypochlorite solution strength after {t} days: {C_final:.4f} %w/w")
    print(f"Chlorate concentration in chemical product: {chlorate_g_l:.4f} g/L")
    print(f"Chlorate concentration in water stream: {chlorate_stream:.4f} mg/L")
    print(f"Sodium hypochlorite dose rate: {dose_rate:.4f} L/hr")
    print(f"Maximum allowable chlorine dose (keeping chlorate < 0.7 mg/L): {max_chlorine:.2f} mg/L")
    print(f"\nMaximum storage time before:")
    print(f"  1. Chlorate in water stream exceeds 0.7 mg/L or")
    print(f"  2. Dose rate exceeds pump max capacity: {max_storage} days")

if __name__ == "__main__":
    main()