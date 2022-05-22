
import threading
import time
import _thread

def run(i):
    time.sleep(10)
    print ("function called by thread %i, name: %s" % (i, threading.current_thread().getName()))

threads = []

def test_thread_consctructor():
    for i in range(5):
        t = threading.Thread(name="thread %d" % i, target=run, args=(i,))
        threads.append(t)
        t.start()
        t.join()

class _Thread(threading.Thread):
    def __init__(self, id, name, counter):
        threading.Thread.__init__(self)
        self.id = id
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting " + self.name)
        print_time(self.name, self.counter, 5)
        print("Exiting " + self.name)

exitFlag = 0

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            _thread.exit()
        time.sleep(delay)
        print("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


if __name__=="__main__":
    # test_thread_consctructor()
    # Create new threads
    thread1 = _Thread(1, "Thread-1", 1)
    thread2 = _Thread(2, "Thread-2", 2)

    # Start new Threads
    thread1.start()
    thread2.start()

    # 以下两行为译者添加，如果要获得和图片相同的结果，
    # 下面两行是必须的。疑似原作者的疏漏
    thread1.join()
    thread2.join()
    print("Exiting Main Thread")
