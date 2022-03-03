def naive(x, y):
    r = x
    for i in range(0, y-1):
        x += r
    return x

print(naive(10, 10))