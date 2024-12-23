import threading

lock = threading.Lock()

def print_numbers():
    for i in range(1, 11):
        with lock:
            print(f"Number: {i}")

def print_squares():
    for i in range(1, 11):
        with lock:
            print(f"Square of {i}: {i**2}")

thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_squares)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Both threads have finished execution.")
