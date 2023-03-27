# Необходимо создать два параллельных потока, каждый из которых выводил бы на экран числа
# от 10 до 1 в обратном порядке с интервалом в одну секунду.
# В выводе должно быть понятно какая нить выполняется, и когда каждая из них начинает и заканчивает своё выполнение.


import threading
import time
lock = threading.Lock()

def flow1(interval):
    for i in range(10, 0, -1):
        lock.acquire()
        print("Поток 1:", i)
        time.sleep(interval)
        lock.release()

def flow2(interval):
    for i in range(10, 0, -1):
        lock.acquire()
        print("Поток 2:", i)
        time.sleep(interval)
        lock.release()

thread1 = threading.Thread(target=flow1, args=(1,))
thread2 = threading.Thread(target=flow2, args=(1,))

thread1.start()
thread2.start()
thread1.join()
thread2.join()
