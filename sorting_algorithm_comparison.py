import tkinter as tk
from tkinter import ttk
import random
import time
from time import perf_counter

# Sorting algorithms

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
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def quick_sort_median(arr):
    if len(arr) <= 1:
        return arr
    if len(arr) < 3:
        return quick_sort(arr)
    mid_index = len(arr) // 2
    median_of_three = [arr[0], arr[mid_index], arr[-1]]
    pivot = sorted(median_of_three)[1]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Generate random data based on user input size
def generate_data(size):
    return [random.randint(0, 10000) for _ in range(1, size+1)]

# Measure sorting time
def measure_time1(sort_func, data):
    start_time = time.time()
    sort_func(data.copy())
    end_time = time.time()
    return end_time - start_time

def measure_time(sort_func, data):
    start_time = perf_counter()
    sort_func(data.copy())  # Copy data to ensure each sort starts with the same input
    end_time = perf_counter()
    return end_time - start_time

# GUI

def create_gui():
    def run_algorithm():
        selected_algorithms = [algorithm_comboboxes[i].get() for i in range(len(algorithm_comboboxes))]
        size = int(input_size_entry.get())

        data = generate_data(size)
        print(data, "\n")
        result_text = ""
        print('\nNew iteration')
        for algorithm_name in selected_algorithms:
            
            if algorithm_name == "Merge Sort":
                time_taken = measure_time(merge_sort, data)
                print("Run time for Merge Sort:", time_taken, 'seconds')
            elif algorithm_name == "Heap Sort":
                time_taken = measure_time(heap_sort, data)
                print("Run time for Heap Sort:", time_taken, 'seconds')
            elif algorithm_name == "Quick Sort":
                time_taken = measure_time(quick_sort, data)
                print("Run time for Quick Sort:", time_taken, 'seconds')
            elif algorithm_name == "Quick Sort (Median of 3)":
                time_taken = measure_time(quick_sort_median, data)
                print("Run time for Quick Sort (Median of 3):)", time_taken, 'seconds')
            elif algorithm_name == "Insertion Sort":
                time_taken = measure_time(insertion_sort, data)
                print("Run time for Insertion Sort:", time_taken, 'seconds')
            elif algorithm_name == "Selection Sort":
                time_taken = measure_time(selection_sort, data)
                print("Run time for Selection Sort:", time_taken, 'seconds')
            elif algorithm_name == "Bubble Sort":
                time_taken = measure_time(bubble_sort, data)
                print("Run time for Bubble Sort:", time_taken, 'seconds')
            result_text += f"Runtime for {algorithm_name}: {time_taken:.9f} seconds\n"

        result_label.config(text=result_text)

    def add_algorithm_combobox():
        new_algorithm_combobox = ttk.Combobox(root, values=algorithms, state="readonly")
        new_algorithm_combobox.grid(row=len(algorithm_comboboxes) + 4, column=0, padx=10, pady=5)
        algorithm_comboboxes.append(new_algorithm_combobox)

    root = tk.Tk()
    root.title("Sorting Algorithm Comparison")

    algorithm_label = ttk.Label(root, text="Select Algorithm(s):")
    algorithm_label.grid(row=0, column=0, padx=10, pady=5)

    algorithms = [
        "Merge Sort",
        "Heap Sort",
        "Quick Sort",
        "Quick Sort (Median of 3)",
        "Insertion Sort",
        "Selection Sort",
        "Bubble Sort"
    ]
    algorithm_comboboxes = []
    initial_algorithm_combobox = ttk.Combobox(root, values=algorithms, state="readonly")
    initial_algorithm_combobox.grid(row=0, column=1, padx=10, pady=5)
    algorithm_comboboxes.append(initial_algorithm_combobox)

    add_algorithm_button = ttk.Button(root, text="Add Algorithm", command=add_algorithm_combobox)
    add_algorithm_button.grid(row=0, column=2, padx=10, pady=5)

    input_size_label = ttk.Label(root, text="Input Size:")
    input_size_label.grid(row=1, column=0, padx=10, pady=5)

    input_size_entry = ttk.Entry(root)
    input_size_entry.grid(row=1, column=1, padx=10, pady=5)

    run_button = ttk.Button(root, text="Run Algorithm(s)", command=run_algorithm)
    run_button.grid(row=2, column=0, columnspan=3, padx=10, pady=5)

    result_label = ttk.Label(root, text="", wraplength=400)
    result_label.grid(row=3,column=0, columnspan=3, padx=10, pady=(20, 10))  # Adjusted padding

    root.mainloop()

create_gui()
