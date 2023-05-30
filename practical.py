import random
import time

def generate_data(size):
    data = [random.randint(1, 100) for _ in range(size)]
    return data

def linear_search_recursive(data, target, index=0):
    if index >= len(data):
        return -1
    elif data[index] == target:
        return index
    else:
        return linear_search_recursive(data, target, index + 1)

def linear_search_non_recursive(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

def binary_search_recursive(data, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2
    if data[mid] == target:
        return mid
    elif data[mid] < target:
        return binary_search_recursive(data, target, mid + 1, high)
    else:
        return binary_search_recursive(data, target, low, mid - 1)

def binary_search_non_recursive(data, target):
    low, high = 0, len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Define the data sizes
# data_sizes = [100, 1000, 10000, 100000]
data_sizes = [100000]

# Run the search algorithms and record the times
results = []
target = 70  # Change the target value here if desired

for size in data_sizes:
    data = generate_data(size)
    
    # Linear Search - Recursive
    start_time = time.time()
    linear_search_recursive(data, target)
    end_time = time.time()
    linear_recursive_time = end_time - start_time

    # Linear Search - Non-Recursive
    start_time = time.time()
    linear_search_non_recursive(data, target)
    end_time = time.time()
    linear_non_recursive_time = end_time - start_time

    # Binary Search - Recursive
    data.sort()  # Binary search requires sorted data
    start_time = time.time()
    binary_search_recursive(data, target, 0, len(data) - 1)
    end_time = time.time()
    binary_recursive_time = end_time - start_time

    # Binary Search - Non-Recursive
    start_time = time.time()
    binary_search_non_recursive(data, target)
    end_time = time.time()
    binary_non_recursive_time = end_time - start_time

    results.append((size, linear_recursive_time, linear_non_recursive_time, binary_recursive_time, binary_non_recursive_time))

# Tabulate the results
print("Data Size\tLinear Recursive\tLinear Non-Recursive\tBinary Recursive\tBinary Non-Recursive")
for result in results:
    size, linear_recursive_time, linear_non_recursive_time, binary_recursive_time, binary_non_recursive_time = result
    print(f"{size}\t\t{linear_recursive_time}\t\t{linear_non_recursive_time}\t\t{binary_recursive_time}\t\t{binary_non_recursive_time}")
