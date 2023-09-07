def fun(n):
    if(n>0):
        print(n,end=" ")
        fun(n-1)
def fun2(n):
    if(n>0):
        fun2(n-1)
        print(n,end=" ")
        
fun(5)
print()
fun2(5)

