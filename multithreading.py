import threading

def home():
    for i in range(10):
        print("thread",i)

def house():
    for i in range(10):
        print("thread-2",i)

threading.Thread(target=home).start()
threading.Thread(target=house).start()
print(threading.active_count())