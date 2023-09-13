# ---------------------------------------------------------------------------- #
#!                            Using Pascal Triangle                            #
# ---------------------------------------------------------------------------- #


def C(n,r):
    if(n == r or r == 0):
        return 1
    return C(n-1,r-1)+C(n-1,r)
n = int(input())
r = int(input())


if(n<r or n<0 or r<0):
    print("\n\n\tInvalid\n\n")

elif(n == r or r == 0):
    print("\n\n 1 \n\n")
else:
    print(C(n,r))
