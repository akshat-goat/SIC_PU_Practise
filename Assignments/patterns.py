def right_angled_triangle(n):
    for i in range(1, n + 1):
        print('*' * i)

def equilateral_triangle(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '* ' * (i + 1))

def hollow_square(n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

def hollow_rhombus(n):
    for i in range(n):
        print(' ' * (n - i - 1), end='')
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

def pascals_triangle(n):
    for i in range(n):
        print(' ' * (n - i), end='')
        num = 1
        for j in range(i + 1):
            print(num, end=' ')
            num = num * (i - j) // (j + 1)
        print()

def x_shape(n):
    for i in range(n):
        for j in range(n):
            if j == i or j == n - i - 1:
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

def x_inside_hollow_square(n):
    mid = n // 2
    for i in range(n):
        for j in range(n):
            if (i == 0 or i == n - 1 or j == 0 or j == n - 1 or
                i == j or j == n - i - 1):
                if i == mid and j == mid:
                    print('0', end=' ')
                else:
                    print('*', end=' ')
            else:
                print(' ', end=' ')
        print()

def benzene_ring(n):
    # Approximate hexagon pattern using stars
    space = n
    for i in range(n):
        print(' ' * space + '* ' * n)
        space -= 1
    for i in range(n):
        print(' ' * (i + 1) + '* ' * n)

n = int(input("Enter the number of lines (>=5 recommended for better patterns): "))
    
print("\nA. Right Angled Triangle:")
right_angled_triangle(n)
    
print("\nB. Equilateral Triangle:")
equilateral_triangle(n)
    
print("\nC. Hollow Square:")
hollow_square(n)
    
print("\nD. Hollow Rhombus:")
hollow_rhombus(n)
    
print("\nE. Pascal's Triangle:")
pascals_triangle(n)
    
print("\nF. X Shape:")
x_shape(n)
    
print("\nG. X inside Hollow Square with 0 at center:")
x_inside_hollow_square(n)
    
print("\nH. Benzene Ring (Approx. Hexagon):")
benzene_ring(n)
