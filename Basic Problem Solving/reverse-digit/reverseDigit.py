def reverseDigit(num):
    res = 0
    while num > 0:
        ld = num%10
        res = res * 10 + ld
        num = num//10
    return res

print(reverseDigit(5376))