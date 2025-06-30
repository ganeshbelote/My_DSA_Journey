# Armstrong number is a number that is equal to the sum of powers to its length of each digit
# => Let assume num = 153 , here length = 3
# => since product = 1^3 + 5^3 + 3^3 --> digit1^length + digit2^length + ...
# => if product == num then num is armstrong number

def isArmstrong(num):
    k = len(str(num))
    dup = num
    res = 0
    while num > 0:
        digit = num%10
        res = res + (digit ** k)
        num = num//10
    
    if dup == res :
        return True
    else:
        return False

print(isArmstrong(153))
print(isArmstrong(123))
