import threading

def home():
    for i in range(100):
        print("thread",i)

def house():
    for i in range(100):
        print("thread-2",i)

threading.Thread(target=home).start()
threading.Thread(target=house).start()
print("thread active count",threading.active_count())
print("program completed")
