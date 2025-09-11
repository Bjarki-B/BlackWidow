#===================== import packages =====================

import numpy as np

#==================== define parameters ====================

# Scaling factors from Curti+2020: Table 2
coeffitients_dic = {
    # for relating to Name Tags check Table 1
    "R2":   {"coeffs": [0.435, -1.362, -5.655, -4.851, -0.478, 0.736], "RMS": 0.11, "sigma": 0.10},
    "R3":   {"coeffs": [-0.277, -3.549, -3.593, -0.981],               "RMS": 0.09, "sigma": 0.07},
    "O3O2": {"coeffs": [-0.691, -2.944, -1.308],                       "RMS": 0.15, "sigma": 0.14},
    "R23":  {"coeffs": [0.527, -1.569, -1.652, -0.421],                "RMS": 0.06, "sigma": 0.12},
    "N2":   {"coeffs": [-0.489, 1.513, -2.554, -5.293, -2.867],        "RMS": 0.16, "sigma": 0.10},
    "O3N2": {"coeffs": [0.281, -4.765, -2.268],                        "RMS": 0.21, "sigma": 0.09},
    "S2":   {"coeffs": [-0.442, -0.360, -6.271, -8.339, -3.559],       "RMS": 0.11, "sigma": 0.06},
    "RS32": {"coeffs": [-0.054, -2.546, -1.970, 0.082, 0.222],         "RMS": 0.07, "sigma": 0.08},
    "O3S2": {"coeffs": [0.191, -4.292, -2.538, 0.053, 0.332],          "RMS": 0.17, "sigma": 0.11},
}

#==================== define functions ====================

def line_ratios(metallicity: float) -> Dict[str, float]:
    """
    Compute log(R) for all diagnostics given metallicity 12 + log(O/H).
    
    Returns a dict: {diagnostic: value}
    """
    x = metallicity - 8.69
    results = {}
    for name, data in coeffitients.items():
        coeffs = data["coeffs"]
        results[name] = np.polyval(list(reversed(coeffs)), x)
    return results

    
