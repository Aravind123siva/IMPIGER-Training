import numpy as np
import time

arr = np.random.rand(10**6)

def sum_with_loop(arr):
    total = 0
    for num in arr:
        total += num
    return total

def sum_with_numpy(arr):
    return np.sum(arr)

start_time = time.time()
loop_sum = sum_with_loop(arr)
loop_time = time.time() - start_time

start_time = time.time()
numpy_sum = sum_with_numpy(arr)
numpy_time = time.time() - start_time

print(f"Sum using for loop: {loop_sum:.6f}, Time: {loop_time:.6f} sec")
print(f"Sum using NumPy: {numpy_sum:.6f}, Time: {numpy_time:.6f} sec")
print(f"NumPy is ~{loop_time / numpy_time:.2f} times faster!")
