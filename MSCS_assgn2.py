import random
import timeit
import tracemalloc

# Quick Sort implementation
def quick_sort(A):
    if len(A) <= 1:
        return A
    pivot = A[len(A) // 2]
    left = [x for x in A if x < pivot]
    middle = [x for x in A if x == pivot]
    right = [x for x in A if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Merge Sort implementation
def merge_sort(A):
    if len(A) <= 1:
        return A
    mid = len(A) // 2
    left = merge_sort(A[:mid])
    right = merge_sort(A[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Function to measure performance using timeit and tracemalloc
def performance(sort_fn, data):
    # Timeit for execution time
    execution_time = timeit.timeit(lambda: sort_fn(data[:]), number=1)

    # Tracemalloc for memory usage
    tracemalloc.start()
    sort_fn(data[:])  # Run the sorting function
    _, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return execution_time, peak_memory / (1024 * 1024)  # Convert to MB

# Generate datasets
random_data = random.sample(range(100000), 10000)
sorted_data = sorted(random_data)
reverse_sorted_data = sorted_data[::-1]

# Test Quick Sort
print("Quick Sort Performance:")
qs_random_time, qs_random_memory = performance(quick_sort, random_data)
qs_sorted_time, qs_sorted_memory = performance(quick_sort, sorted_data)
qs_reverse_time, qs_reverse_memory = performance(quick_sort, reverse_sorted_data)

print(f"Random data: {qs_random_time:.6f} seconds, {qs_random_memory:.6f} MB")
print(f"Sorted data: {qs_sorted_time:.6f} seconds, {qs_sorted_memory:.6f} MB")
print(f"Reverse sorted data: {qs_reverse_time:.6f} seconds, {qs_reverse_memory:.6f} MB")

# Test Merge Sort
print("\nMerge Sort Performance:")
ms_random_time, ms_random_memory = performance(merge_sort, random_data)
ms_sorted_time, ms_sorted_memory = performance(merge_sort, sorted_data)
ms_reverse_time, ms_reverse_memory = performance(merge_sort, reverse_sorted_data)

print(f"Random data: {ms_random_time:.6f} seconds, {ms_random_memory:.6f} MB")
print(f"Sorted data: {ms_sorted_time:.6f} seconds, {ms_sorted_memory:.6f} MB")
print(f"Reverse sorted data: {ms_reverse_time:.6f} seconds, {ms_reverse_memory:.6f} MB")
