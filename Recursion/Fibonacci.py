# ---------------------------------------------------------------------------- #
# !                       Optimized Recursion Fibonacci                        #
# ---------------------------------------------------------------------------- #

n = int(input())

f = [-1 for i in range(n)]

# print(f)
def fib(n):
    if(n <= 1):
        f[n] = n;
        return n;
    

    else:
        if(f[n-2] == -1) :
            f[n-2] = fib(n-2)
        if(f[n-1] == -1) :
            f[n-1] = fib(n-1)
    print((f[n-2]+f[n-1]), end = " ")
    return f[n-2]+f[n-1]
print("0 1 ",end="")

fib(n)