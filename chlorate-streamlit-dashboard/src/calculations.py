def fahrenheit(T_celsius):
    return ((T_celsius * 9 / 5) + 32)

def decomposition_rate_constant(T_celsius):
    ln_k = 18.56 * math.log((fahrenheit(T_celsius)) + 460) - 129.26
    k = math.exp(ln_k)
    return k

def calculate_remaining_hypochlorite(C0, k, days):
    return remaining_hypochlorite(C0, k, days)

def calculate_chlorate_formed(C0, C_final, initial_chlorate_g_l):
    return chlorate_formed(C0, C_final, initial_chlorate_g_l)

def calculate_dose_rate(chlorine_dose_mg_l, C_final, water_flow_MLD):
    return sodium_hypochlorite_dose_rate(chlorine_dose_mg_l, C_final, water_flow_MLD)

def calculate_chlorate_in_stream(chlorate_g_l, chlorine_dose_mg_l, C_final):
    return chlorate_in_water_stream(chlorate_g_l, chlorine_dose_mg_l, C_final)

def calculate_max_chlorine_dose(C_final, chlorate_g_l):
    return max_chlorine_dose(C_final, chlorate_g_l)

def calculate_max_storage_time(C0, initial_chlorate_g_l, chlorine_dose_mg_l, pump_max_l_hr, water_flow_MLD, T_celsius):
    return find_max_storage_time(C0, initial_chlorate_g_l, chlorine_dose_mg_l, pump_max_l_hr, water_flow_MLD, T_celsius)