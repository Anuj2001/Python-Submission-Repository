li=list(map(int,input("Enter a sequence of integers:").split()))
print("Positive Integers are:",end="")
n=len(li)
for i in range(n):
    if(li[i]>0): # Cheking for positive integers.
        print(li[i],end=" ")
