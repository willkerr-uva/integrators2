import numpy as np
import matplotlib.pyplot as plt
from math import pi, gamma

def mc_volume(d, N):
    r = 1
    points = np.random.uniform(-r, r, size=(N, d))
    squared_distances = np.sum(points**2, axis=1)
    n_hits = np.sum(squared_distances <= r**2)
    
    v_cube = (2*r)**d
    prob = n_hits / N
    v = v_cube * prob
    return v

def exact_volume(d, r):
    return (pi**(d/2) * r**d) / gamma(d/2 + 1)

def analyze(d_values, N_values, R=20):
    r = 1
    plt.figure(figsize=(8,6))
    sqrt_N_values = np.sqrt(N_values)

    for d in d_values:
        frac_error_means = []
        frac_error_stds = []

        for N in N_values:
            frac_errors = []
            for _ in range(R):
                vol_est = mc_volume(d, N)
                vol_exact = exact_volume(d, r)
                frac_error = abs(vol_est - vol_exact) / vol_exact
                frac_errors.append(frac_error)

            frac_error_means.append(np.mean(frac_errors))
            frac_error_stds.append(np.std(frac_errors))
        plt.errorbar(
            sqrt_N_values,
            frac_error_means,
            yerr=frac_error_stds,
            marker='o',
            linestyle='-',
            label=f'd={d}'
        )

    plt.yscale('log')
    plt.xlabel('sqrt(N)')
    plt.ylabel('Fractional error')
    plt.title('Monte Carlo Convergence for d-dimensional Spheres')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.tight_layout()
    plt.savefig('convergence.png', dpi=300)
    plt.show()

if __name__ == "__main__":
    N_values = 2**np.arange(6, 25)
    d_values = [2, 3, 5]
    analyze(d_values, N_values, R=20)
