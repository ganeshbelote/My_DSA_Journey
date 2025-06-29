def palindromeCheck(num):
    dup = num
    rev = 0
    while num > 0:
        ld = num%10
        rev = rev * 10 + ld
        num = num//10
    
    if rev == dup:
        return True
    else:
        return False

print(palindromeCheck(3773))
print(palindromeCheck(1230))
