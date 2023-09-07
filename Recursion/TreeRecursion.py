def fun(n):
    if n==0:
        return 0
    print(n, end=" ")
    fun(n-1)
    print()
    fun(n-1)
    
def fun2(n):
    if n==0:
        return 0
    fun2(n-1)
    print()
    fun2(n-1)
    print(n, end=" ")
fun(3)
print("\nHead")

fun2(3)