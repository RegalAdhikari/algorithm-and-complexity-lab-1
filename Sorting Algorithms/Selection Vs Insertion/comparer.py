import time
import matplotlib.pyplot as plt
import numpy as np

from random import randint


from selection_sort import selection_sort
from insertion_sort import insertion_sort

start = time.time()
print("Sorting started")
n = 1000 # Number of arrays
size = 5 # Size of each array

xpoints = [5]
ypoints = [0]
for i in range(n):
    A = [randint(0, 100) for _ in range(size)]
    insertion_sort(A)
    xpoints.append(size)
    ypoints.append(time.time() - start)
    size = size + 1
print("\n")
print("Time taken for insertion sort: ", time.time() - start)

# For selection sort
start = time.time()
size = 5 # Size of each array
x2points = [5]
y2points = [0]
for i in range(n):
    A = [randint(0, 100) for _ in range(size)]
    selection_sort(A)
    x2points.append(size)
    y2points.append(time.time() - start)
    size = size + 1
    
print("\n")
print("Time taken for selection sort: ", time.time() - start)
plt.xlabel('Input Size')
plt.ylabel('Execution Time (seconds)')
plt.title('Input Size vs Execution Time')
plt.plot(xpoints, ypoints,label = "Insertion Sort")
plt.plot(x2points, y2points,label = "Selection Sort")
plt.legend()
plt.show()