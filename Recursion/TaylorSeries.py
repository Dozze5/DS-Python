p = 1.0
f = 1.0

def e(x,n):
    global p , f
    if(n == 0):
        return 0
    r = e(x,n-1)
    p *= x
    f *= n
    return r+p/f

print(e(4,15))


# ---------------------------------------------------------------------------- #
#                           Tayler Series Horner Rule                          #
# ---------------------------------------------------------------------------- #


s = 1.0

def Horner(x , n):
    global s
    if(n == 0):
        return s
    s = 1+ x*s/n
    return Horner(x,n-1)

print(Horner(4,15))