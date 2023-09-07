x = 0

def fun(n):
    global x
    if n==0:
        return 0
    x = x+1
    return fun(n-1) + x
print(fun(5))

