# Write code for algorithm 2 belowdef print_natural_numbers(n):
def print_natural_numbers(n):
    if n < 1:
        print("Please provide a positive integer greater than or equal to 1.")
    else:
        for i in range(1, n + 1):
            print(i)

print_natural_numbers(5)
