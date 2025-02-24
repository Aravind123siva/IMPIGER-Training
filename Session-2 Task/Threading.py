import threading
import time
def even_number():
    for i in range(10):
        print(i)
        time.sleep(1)
    print("Thread1 completed")
def odd_number():
    for i in range(20):
        print(i)
        time.sleep(1)
    print("Thread2 completed")
thread1= threading.Thread(target=even_number)
thread2= threading.Thread(target=odd_number)
thread1.start()
thread2.start(
thread1.join()
thread2.join()
print("Both the tasks are completed")