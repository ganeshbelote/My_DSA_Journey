def palindrome(str):
    start = 0
    end = len(str) - 1

    while start < end:
        if str[start].lower() != str[end].lower():
            return False
        start += 1
        end -= 1
    
    return True

def palindromeEnhanced(str):
    start = 0
    end = len(str) - 1

    while start < end:
        if str[start].lower() != str[end].lower():
            return False
        elif not str[start].isalnum():
            start += 1
        elif not str[end].isalnum():
            end -= 1
        else:
            start += 1
            end -= 1
    
    return True

print(palindromeEnhanced("madam"))
print(palindromeEnhanced("Madam"))
print(palindromeEnhanced("ganesh"))
print(palindromeEnhanced("A man, a plan, a canal: Panama"))
