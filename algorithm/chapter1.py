from data_struct import Stack


# 正整数10进制转2进制
def divideBy2(decimalNumber):
    remainStack = Stack()

    while decimalNumber > 0:
        remain = decimalNumber % 2
        remainStack.push(remain)
        decimalNumber = decimalNumber // 2  # 除2取整

    binString = ""
    while not remainStack.is_empty():
        binString += str(remainStack.pop())

    return binString


if __name__ == "__main__":
    print(divideBy2(64))
