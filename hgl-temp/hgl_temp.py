#!/usr/bin/env python

import numpy as np

def predict_hgl(Q=300,
                W_o=0.8,
                H_o=2.0,
                L=3.6,
                W=2.4,
                H=2.4,
                T_inf=20,
                delta=0.016,
                k=0.48,
                rho=1440,
                c_p=840,
                t=300):

    # Normalize thermal conductivity
    k = k / 1000

    # Thermal diffusivity (m^2/s)
    alpha = k / (rho * c_p)

    # Thermal penetration time (s)
    t_p = delta**2 / (4 * alpha)

    # Effective heat transfer coefficient (kW/m^2-K)
    if t < t_p:
        h_k = np.sqrt(k * rho * c_p / t)
    elif t >= t_p:
        h_k = (k / delta)

    # Ventilation area (m^2)
    A_o = W_o * H_o

    # Total area (m^2)
    A_T = (2 * L * W) + (2 * L * H) + (2 * W * H) - (A_o)

    # Change in gas temperature
    delta_T = 6.85 * (Q**2 / (A_o * np.sqrt(H_o) * h_k * A_T))**(1/3)

    # Actual gas temperature
    T_gas = delta_T + T_inf

    return T_gas


if __name__ == "__main__":
    predict_hgl()
