# Write code for algorithm 1 below def countdown(n):
def countdown(n):
    if n < 0:
        print("Please enter a positive number.")
    else:
        for i in range(n, -1, -1):
            print(i)

# Get user input
try:
    n = int(input("Enter a positive number: "))
    countdown(n)
except ValueError:
    print("Invalid input. Please enter a positive number.")