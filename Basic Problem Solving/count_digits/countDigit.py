import math
def countDigit(num) :
    return int(math.log10(num) + 1)

def bruteForcecountDigit(num) :
    cnt = 0
    while num > 0:
        num = num//10
        cnt += 1
    return cnt

ans = countDigit(4368)
ans2 = bruteForcecountDigit(4368)
print(ans,ans2)