def fib(n,memo=None):
    if memo is None:
        memo={}
    if n in memo:
        return memo[n]
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        memo[n]=fib(n-1,memo)+fib(n-2,memo)
        return memo[n]
try:
    num=int(input("Enter the value of n to find the nth fibonacci number:"))
    if num<0:
        print("Please enter a non-negative number")
    else:
        result=fib(num)
        print(f"The {num}th fibonacci number is:{result}")
except ValueError:
    print("Invalid input")
