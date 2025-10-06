import numpy as np
import matplotlib.pyplot as plt
from math import pi, gamma

def mc_volume(d, N):
    r=1
    points = np.random.uniform(-r, r, size=(N, d))

    squared_distances = np.sum(points**2, axis=1)
    n_hits = np.sum(squared_distances <= r**2)
    
    v_cube = (2*r)**d
    prob = n_hits / N
    v = v_cube * prob
    
    if prob > 0 and prob < 1:
        stdev = v_cube * np.sqrt(prob * (1 - prob) / N)
    else:
        stdev = 0.0

    return v, stdev

def exact_volume(d, r):
    return (pi**(d/2) * r**d) / gamma(d/2 + 1)

def analyze(d_values, N_values):
    r=1
    plt.figure(figsize=(8,6))
    for d in d_values:
        frac_errors = []
        error_bars = []
        for N in N_values:
            vol_est, stdev = mc_volume(d, N, r)
            vol_exact = exact_volume(d, r)
            
            frac_error = abs(vol_est - vol_exact) / vol_exact
            frac_errors.append(frac_error)
            error_bars.append(stdev / vol_exact)

        plt.errorbar(N_values, frac_errors, yerr=error_bars, 
                     marker='o', linestyle='-', label=f'd={d}')
    
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Number of points N')
    plt.ylabel('Fractional error')
    plt.title('Monte Carlo Convergence for d-dimensional Spheres')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.tight_layout()
    plt.savefig('convergence.png', dpi=300)
    plt.show()

if __name__ == "__main__":
    N_values = [10, 50, 100, 500, 1000, 5000, 10000]
    d_values = [2, 3, 5]
    analyze(d_values, N_values)
