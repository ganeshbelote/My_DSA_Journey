# The Fibonacci sequence is a series of numbers where:
# Each number is the sum of the two previous numbers.
# It starts with:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
# For position n (starting from 0):
# F(0) = 0  
# F(1) = 1  
# F(n) = F(n - 1) + F(n - 2) for n ≥ 2

def Fibonacci(num):
    if num == 0:
        return [0]
    if num == 1:
        return [1]
    fib = [0,1]
    for i in range(2,num):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib

print(Fibonacci(6))