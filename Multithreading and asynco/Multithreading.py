import threading


def fibonacci(n):
    series = [0, 1]
    for i in range(2, n):
        series.append(series[-1] + series[-2])
    print(f"{threading.current_thread().name}: Fibonacci series for {n}: {series}")


def main():
    values = [10, 15, 20, 25, 30]

    for i, val in enumerate(values):
        thread = threading.Thread(target=fibonacci, args=(val,), name=f"Thread-{i + 1}")
        thread.start()
        thread.join()




result = main()
print(result)
￼
