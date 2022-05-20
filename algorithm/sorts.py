
import random


def bubbleSort(a):
    length = len(a)
    for i in range(length):
        for j in range(i + 1, length):
            if (a[j] < a[i]):
                swap(a, i, j)

def insertSort(a):
    length = len(a)
    for i in range(1, length):
        value = a[i]
        j = i - 1
        while j >= 0 and a[j] > value:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = value

def swap(a, i, j):
    print("swap index %d (%d) with index %d (%d)"
        % (i, a[i], j, a[j]))
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp

def printList(a):
    line = ""
    for i in a:
        line += str(i) + " "
    print(line)

def prepareRandomList():
    random.seed(54)
    return [random.randint(0,100) for _ in range(10)]


if __name__=="__main__":
    # a = [9,7,8,62,5,4,3,2,1]
    a = prepareRandomList()
    print("sort started.")
    insertSort(a)
    printList(a)
    print("sort finished.")