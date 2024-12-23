import threading
import queue

shared_queue = queue.Queue()

def write_to_queue():
    for i in range(10):
        shared_queue.put(f"Item {i}")
        print(f"Written: Item {i}")

def read_from_queue():
    while True:
        if not shared_queue.empty():
            item = shared_queue.get()
            print(f"Read: {item}")
        else:
            break

write_thread = threading.Thread(target=write_to_queue)
read_thread1 = threading.Thread(target=read_from_queue)
read_thread2 = threading.Thread(target=read_from_queue)

write_thread.start()
read_thread1.start()
read_thread2.start()

write_thread.join()
read_thread1.join()
read_thread2.join()

print("Program finished.")
