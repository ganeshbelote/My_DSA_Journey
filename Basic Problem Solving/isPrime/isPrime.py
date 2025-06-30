import math

def isPrime(num):
    if (num == 2):
        return "2 is niether be prime nor be composite"
    sqrt = int(math.sqrt(num))
    for i in range(2,sqrt + 1):
        if num%i == 0:
            return False
    return True

print(isPrime(36))
print(isPrime(17))
print(isPrime(3))

