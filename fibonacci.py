# 0,1,1,2,3,5,8,13
import time


def fib1(l):  # iterative
    num1 = 0
    num2 = 1
    s = 0
    for i in range(0, l):
        s = num1 + num2
        num2 = num1
        num1 = s
    return num1


def fib2(n):  # recursive
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib2(n - 1) + fib2(n - 2)


def fib3(n):
    mem = {0: 0, 1: 1}

    def fibo(n):
        if n in mem:
            return mem[n]
        else:
            mem[n] = fibo(n - 1) + fibo(n - 2)
            return mem[n]

    fibo(n)


def timer(fun, n, messaage=''):
    time0 = time.time_ns()
    fun(n)
    time1 = time.time_ns()
    print('The time taken for the ', messaage, ' function is')
    print(time1 - time0)


if __name__ == '__main__':
    timer(fib1, 700, 'Iterative')
    timer(fib2, 25, 'recursive')
    timer(fib3, 700, 'dynamic')