def Power(m,n):
    if(n == 0):
         return 1
    return Power(m , n-1)*m

print(Power(2,9))

def Power2(m,n):
    if(n == 0):
         return 1
    if(n%2 == 0):
        return Power2(m*m , n/2)
    else:
        return m* Power2(m*m , (n-1)/2)