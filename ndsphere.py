import sys
import numpy as np

def main():
    # Check if the user provided the correct number of arguments
    if len(sys.argv) != 4:
        # Note: The prompt shows d, N, r, but the image implies d, r, N.
        # This code follows the starter code's d, N, r order.
        print(f"Usage: {sys.argv[0]} <dimension d> <points N> <radius r>")
        sys.exit(1)  # Exit with error code

    # Parse the command-line arguments
    try:
        d = int(sys.argv[1])      # Dimension
        N = int(sys.argv[2])      # Number of points
        r = float(sys.argv[3])    # Radius

    except ValueError:
        print("Error: Please provide valid integers and a float as arguments.")
        sys.exit(1)  # Exit with error code

    # ******* Add your code here

    #N random points
    points = np.random.uniform(-r, r, size=(N, d))
    
    #determine number in sphere 
    squared_distances = np.sum(points**2, axis=1)
    n_hits = np.sum(squared_distances <= r**2)

    #compute volume of cube, volume of sphere based on fraction of N in sphere
    v_cube = (2 * r)**d
    volume = v_cube * (n_hits / N)

   
    prob = n_hits / N
    
    if prob > 0 and prob < 1:
        stdev = v_cube * np.sqrt(prob * (1 - prob) / N)
    else:
        stdev = 0.0 
        
    if volume > 0:
        relerror = stdev / volume
    else:
        relerror = 0.0

    # *******

    # Do not change the format below
    print(f"(r): {r}")
    print(f"(d,N): {d} {N}")
    print(f"volume: {volume}")
    print(f"stat uncertainty: {stdev}")
    print(f"relative error: {relerror}")

if __name__ == "__main__":
    main()