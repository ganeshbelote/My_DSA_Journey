def pritRandom(num):
    if num == 0:
        return
    print(num)
    pritRandom(num - 1)


pritRandom(6)