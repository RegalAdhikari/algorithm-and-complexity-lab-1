import random
import time
import matplotlib.pyplot as plt
from selection_sort import selection_sort
from insertion_sort import insertion_sort

def generate_random_input(size):
    return [random.randint(1, 1000) for _ in range(size)]

def measure_execution_time(sort_func, input_size):
    arr = generate_random_input(input_size)
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return end_time - start_time

input_sizes = [100, 500, 1000, 2000, 5000]
insertion_sort_times = []
selection_sort_times = []

for size in input_sizes:
    insertion_sort_time = measure_execution_time(insertion_sort, size)
    selection_sort_time = measure_execution_time(selection_sort, size)
    
    insertion_sort_times.append(insertion_sort_time)
    selection_sort_times.append(selection_sort_time)

plt.plot(input_sizes, insertion_sort_times, label='Insertion Sort')
plt.plot(input_sizes, selection_sort_times, label='Selection Sort')
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Input Size vs Execution Time')
plt.legend()
plt.show()
