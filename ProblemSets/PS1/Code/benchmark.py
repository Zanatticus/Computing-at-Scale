import subprocess
import re
import numpy as np
import os

import matplotlib.pyplot as plt

# Path to the binary
binary_path = "./build/matmul"

# Range of N values (2^4 to 2^10)
N_values = [2**i for i in range(4, 11)]

# Number of runs to average over
num_runs = 5

# Store results
inner_product_results = []
outer_product_results = []

# Loop over N values
for N in N_values:
    inner_times = []
    outer_times = []
    
    for _ in range(num_runs):
        print(f"Running for N={N}")
        # Call the binary with the current N value
        result = subprocess.run([binary_path, str(N)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output = result.stdout
        
        # Parse the timing results from the output
        inner_match = re.search(r'Inner product MMM avg\. run time \(ns\): (\d+)', output)
        outer_match = re.search(r'Outer product MMM avg\. run time \(ns\): (\d+)', output)
        
        if inner_match:
            inner_times.append(int(inner_match.group(1)))  # Keep in nanoseconds
        if outer_match:
            outer_times.append(int(outer_match.group(1)))  # Keep in nanoseconds
    
    # Average times for this N
    if inner_times:
        inner_product_results.append(np.mean(inner_times))
    if outer_times:
        outer_product_results.append(np.mean(outer_times))

# Plot the results
plt.figure(figsize=(12, 8))

# Create subplots for better comparison
plt.subplot(2, 1, 1)
plt.plot(N_values, inner_product_results, marker='o', label="Inner Product MMM", color='blue')
plt.xlabel("N (Input Size)")
plt.ylabel("Average Execution Time (ns)")
plt.title("Inner Product Matrix Multiplication - Execution Time vs Input Size")
plt.xscale("log", base=2)
plt.yscale("log")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(N_values, outer_product_results, marker='s', label="Outer Product MMM", color='red')
plt.xlabel("N (Input Size)")
plt.ylabel("Average Execution Time (ns)")
plt.title("Outer Product Matrix Multiplication - Execution Time vs Input Size")
plt.xscale("log", base=2)
plt.yscale("log")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.legend()

plt.tight_layout()

# Create plots directory if it doesn't exist
os.makedirs("plots", exist_ok=True)

plt.savefig("plots/matrix_multiplication_subplots.png", dpi=300, bbox_inches='tight')
plt.close()

# Also create a comparison plot
plt.figure(figsize=(10, 6))
plt.plot(N_values, inner_product_results, marker='o', label="Inner Product MMM", linewidth=2)
plt.plot(N_values, outer_product_results, marker='s', label="Outer Product MMM", linewidth=2)
plt.xlabel("N (Input Size)")
plt.ylabel("Average Execution Time (ns)")
plt.title("Matrix Multiplication Comparison - Execution Time vs Input Size")
plt.xscale("log", base=2)
plt.yscale("log")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.legend()
plt.tight_layout()
plt.savefig("plots/matrix_multiplication_comparison.png", dpi=300, bbox_inches='tight')
plt.close()