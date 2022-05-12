# https://python-parallel-programmning-cookbook.readthedocs.io/zh_CN/latest/chapter1/index.html

from threading import Thread, get_ident
from time import sleep


class CookBook(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.message = "Thread running, id:" + str(get_ident())+ "\n"

    def print_message(self):
        print(self.message)

    def run(self):
        print("Thread Starting\n")
        x = 0
        while (x < 10):
            self.print_message()
            sleep(2)
            x += 1
        print("Thread Ended\n")

# start the main process
print("Process Started")

# create an instance of the HelloWorld class
hello_Python = CookBook()

# print the message...starting the thread
hello_Python.start()

# end the main process
print("Process Ended")
