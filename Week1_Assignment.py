# Print the Triangle pattern
# Create lower triangular, upper triangular and pyramid containing the "*" character.

def print_lower_triangle(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()

def print_upper_triangle(n):
    for i in range(n, 0, -1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()

def print_pyramid(n):
    for i in range(1, n + 1):
        for j in range(n - i):
            print(" ", end="")
        for j in range(1, i + 1):
            print("*", end=" ")
        print()

n = int(input("Enter the number of rows: "))
print("\nLower Triangle:")
print_lower_triangle(n)
print("\nUpper Triangle:")
print_upper_triangle(n)
print("\nPyramid:")
print_pyramid(n)
