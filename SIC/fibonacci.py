nth_number = int(input("Enter the nth number for fibonacci series :"))
if nth_number == 0:
    print("0")
elif nth_number == 1 :
    print("0","1")
else:    
    a, b = 0 , 1
    print(a)
    print(b)
    for i in range (2,nth_number+1):
        next_num = a + b
        a = b
        b= next_num
        print(next_num)