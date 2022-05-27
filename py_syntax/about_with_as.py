'''
https://www.jianshu.com/p/c00df845323c
'''

class A:
    def __enter__(self):
        print("A __enter__ invoked.")
        return self
    def __exit__(self, type, value, trace):
        print("A __exit__ invoked.")
        print(f"type{type}")
        print(f"value{type}")
        print(f"value{trace}")
    def foo():
        return 1/0

def get_A():
    return A()

def io_read_test():
    with open("./plain_text", "r") as file:
        data = file.read()
        print(data)

def io_write_test():
    with open("./plain_text", "a+") as file:
        file.write("\na new line append by io_write_test.")


if __name__=="__main__":
    # io_read_test()
    # io_write_test()
    with get_A() as a:
        # a.foo()
        print(a)