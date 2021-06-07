def do(a, b):
    if a < b:
        return do(b,a)
    elif b != 0:
        return a + do(a,b-1)
    else:
        return 0

print(do(3,4))
