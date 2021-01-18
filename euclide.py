def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)
a = int(input("enter a no 1:"))
b = int(input("enter a no 2:"))
print("the GCD of two no ",gcd(a,b))
