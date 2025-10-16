def fibonacci_loop(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    a,b=0,1
    for _ in range(2,n+1):
        a,b=b,a+b
    return b
try:
    num=int(input("Enter the value of n to find the nth fibonacci number:"))
    if num<0:
        print("Please enter a non-negative integer")
    else:
        result=fibonacci_loop(num)
        print(f"The {num}th fibonacci number is: {result}")
except ValueError:
    print("Invalid input.Please enter an integer")
