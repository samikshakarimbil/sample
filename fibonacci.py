# 0,1,1,2,3,5,8,13

def fib1(l):  # iterative
    num1 = 0
    num2 = 1
    s = 0
    for i in range(0, l):
        print(num1)
        s = num1 + num2
        num2 = num1
        num1 = s


def fib2(n):  # recursive
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib2(n - 1) + fib2(n - 2)


if __name__ == '__main__':
    # print('Hi')
    print(fib2(10))
