from itertools import combinations
from itertools import permutations
from concurrent.futures import ProcessPoolExecutor
import random

def generate_permutations(row):
    return list(set(permutations(row)))

def parallel_permutations(row, num_processes):
    with ProcessPoolExecutor(max_workers=num_processes) as executor:
        futures = [executor.submit(generate_permutations, row) for _ in range(num_processes)]
        #futures = [executor.submit(generate_permutations, row) for _ in range(num_processes)]
    
    all_permutations = []
    for future in futures:
        all_permutations.extend(future.result())

    return (all_permutations)

# Example usage:



if __name__ == '__main__':
    num_ones = 3
    num_zeros = 4
    row = [1] * num_ones + [0] * num_zeros

    num_processes = 2  # Adjust the number of processes based on your system capabilities
    result = parallel_permutations(row, num_processes)
    print(len(result))