n=int(input("Enter the length of Fibonacci series:"))
arr=[0]*n
arr[0]=0 # first member of fibonacci series.
arr[1]=1 # Second member of fibonacci series.
print("\nFibonacci series:",end="")
for i in range(n):
    if(i<2):
        print(arr[i],end=" ") #Initial two members of fibonacci series.
    else:
        arr[i]=arr[i-1]+arr[i-2] #Other Members of Fibonacci series.
        print(arr[i],end=" ")
