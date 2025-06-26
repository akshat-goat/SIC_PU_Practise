a=11
input_number = int(input("Enter the number to print Multiplication Table : "))
for i in range (1,a):
    print('%2d * %02d = %03d' % (input_number,i,(input_number * i)))