# Function definitions

def f(x):
    return x - 1

def g(x):
    return x * 2

def h(x, y):
    return int(str(x) + str(y))


# Solution

print(h(g(g(5)), h(f(f(f(5))), f(5))))
