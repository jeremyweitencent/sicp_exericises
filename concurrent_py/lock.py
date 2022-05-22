import threading

lock = threading.Lock()
share_res_with_lock = 0
share_res_without_lock = 0
COUNT = 1000000


def run1():
    print("thread %d starting" % (1))
    global share_res_without_lock, share_res_with_lock
    for i in range(COUNT):
        share_res_without_lock += 1
        lock.acquire()
        share_res_with_lock += 1
        lock.release()
    print("thread %d finished" % (1))

def run2():
    print("thread %d starting" % (2))
    global share_res_without_lock, share_res_with_lock
    for i in range(COUNT):
        share_res_without_lock -= 1
        lock.acquire()
        share_res_with_lock -= 1
        lock.release()
    print("thread %d finished" % (2))



if __name__=="__main__":
    thread1 = threading.Thread(target=run1)
    thread2 = threading.Thread(target=run2)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("value without lock is %d" % share_res_without_lock)
    print("value with lock is %d" % share_res_with_lock)