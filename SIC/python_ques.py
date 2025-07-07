def f(x):
    return x and f(x-1) or x

print(f(3))