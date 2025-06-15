import random
import timeit

# --- Алгоритм сортування злиттям ---
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# --- Алгоритм сортування вставками ---
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# --- Вимірювання часу виконання (спрощено) ---
def benchmark_sorting_algorithms(sizes):
    algorithms = {
        "Merge Sort": merge_sort,
        "Insertion Sort": insertion_sort,
        "Timsort (sorted)": sorted
    }

    results = {name: [] for name in algorithms}

    for size in sizes:
        data = [random.randint(0, 10000) for _ in range(size)]

        for name, func in algorithms.items():
            arr_copy = data[:]
            exec_time = timeit.timeit(lambda: func(arr_copy), number=1)
            results[name].append(exec_time)

    return results

# --- Виведення результатів ---
def print_results(results, sizes):
    print(f"{'Розмір':>10} | {'Merge Sort':>12} | {'Insertion Sort':>15} | {'Timsort':>10}")
    print("-" * 55)
    for i, size in enumerate(sizes):
        merge = f"{results['Merge Sort'][i]:.6f}"
        insert = f"{results['Insertion Sort'][i]:.6f}"
        tim = f"{results['Timsort (sorted)'][i]:.6f}"
        print(f"{size:>10} | {merge:>12} | {insert:>15} | {tim:>10}")

sizes = [100, 500, 1000, 5000]
results = benchmark_sorting_algorithms(sizes)
print_results(results, sizes)