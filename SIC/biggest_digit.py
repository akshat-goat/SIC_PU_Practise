number = input("Enter the Number :")
biggest_digit = 0
for i in number:
    if int(i) > biggest_digit:
        biggest_digit = int(i)
print("The Biggest digit is : ", biggest_digit)