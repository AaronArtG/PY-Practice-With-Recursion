# Write code for algorithm 3 belowdef fibonacci(n):
def fibonacci(n):
    if n <= 0:
        return "Please enter a positive number."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = 4
result = fibonacci(n)
if isinstance(result, int):
    print(f"The {n}th element in the Fibonacci Sequence is: {result}")
else:
    print(result) 
