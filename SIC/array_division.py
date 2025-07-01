import sys as s
range, x, y = map(int,input("Enter the Range N, X, Y :").split())
if (x + y) != range :
    print("Range limit Exceeds x + y not equal to N")
    s.exit()
numbers = list(map(int,input("Enter the numbers in range n").split()))
numbers.sort()
p = numbers[y]  - numbers[y-1] - 1
print(p)