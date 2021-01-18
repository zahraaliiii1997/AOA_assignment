n = int(input("enter the no u want:"))
result = 1
for i in range(n,0,-1):
    result = result*i

print("factorial of" ,n , "is" ,result)
