""" https://docs.python.org/zh-cn/dev/library/asyncio-task.html """

import asyncio
import datetime

"""
一个协程函数，返回一个协程对象
"""
async def print_delay(msg, delay):
    await asyncio.sleep(delay)
    print(msg)

"""
开启并异步执行一个协程
不是一个协程函数
asyncio.create_task函数,返回的对象是一个“任务”,任务对象会被直接异步执行
"""
def start_corutine_task(task):
    asyncio.create_task(task)

"""
开启并同步执行一个协程
因为需要同步，所以被“传染”成协程函数
"""
async def start_and_await_corutine_task(task):
    await asyncio.create_task(task)

"""
指定*后的参数使用关键字方式传参
e.g. foo(1,b=True)
https://www.zhihu.com/question/287097169
"""
def foo(a, *, b=False):
    pass

"""
可变参数
e.g. foo2("a",a=1,b=2)
"""
def foo2(*a, **b):
    print(a[0])
    for k in b.keys():
        print(k)


async def main():

    # print("task1_insert_start")
    # await start_and_await_corutine_task(print_delay("task1_finish", 0.5))
    # print("task1_insert_done")
    # print("task2_insert_start")
    # start_corutine_task(print_delay("task2_finish", 0.5))
    # print("task2_insert_done")

    # group = asyncio.gather(
    #     print_delay("task1_finish", 0.5),
    #     print_delay("task2_finish", 0.5),
    #     print_delay("task3_finish", 0.5),
    # )
    # try:
    #     group.cancel()
    # except:
    #     pass

    # try:
    #     await asyncio.wait_for(print_delay("task1_finish", 0.5), 0.1)
    # except:
    #     pass

    '''给出时间，让协程执行'''
    await asyncio.sleep(2)
    print(datetime.datetime.now())


if __name__=="__main__":
    asyncio.run(main())