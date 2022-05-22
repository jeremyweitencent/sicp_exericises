
import threading
import time

res = []
condition_p = threading.Condition()
# condition_p = threading.Condition()
# condition_c = threading.Condition()

class consumer(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def consume(self):
        global condition_p, res
        condition_p.acquire()
        while len(res) == 0:
            condition_p.wait()
            print("Consumer[%s] notify : no res to consume" % self.name)
        res.pop()
        print("Consumer[%s] notify : consumed 1 item" % self.name)
        print("Consumer[%s] notify : items to consume are "  % self.name + str(len(res)))

        condition_p.notify()
        condition_p.release()

    def run(self):
        for i in range(0, 5):
            time.sleep(2)
            self.consume()

class producer(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def produce(self):
        global condition_p, res
        global res
        condition_p.acquire()
        while len(res) == 10:
            condition_p.wait()
            print("Producer notify : items producted are " + str(len(res)))
            print("Producer notify : stop the production!!")
        res.append(1)
        print("Producer notify : total items producted " + str(len(res)))
        condition_p.notify()
        condition_p.release()

    def run(self):
        for i in range(0, 10):
            time.sleep(5)
            self.produce()


if __name__=="__main__":
    p = producer()
    c = consumer("c1")
    consumer_ = consumer("c2")
    p.start()
    c.start()
    consumer_.start()
    p.join()
    c.join()
    consumer_.join()