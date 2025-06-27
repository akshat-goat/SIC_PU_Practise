#right angled triangle
n = int(input("Enter thr no. of rows "))
for i in range(n+1):
    print("*"*i)


# Equilateral Triangle
for i in range (n+1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i - 1)
    print(spaces + stars)

