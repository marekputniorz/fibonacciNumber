def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

number = int(input("Please enter a non negative integer: "))

if number < 0:
    print("Number is not valid")

print("\nFibonacci number of "+  str(number) + " is: ",fib(number))

 