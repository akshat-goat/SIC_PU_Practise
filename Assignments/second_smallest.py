number = input("Enter the Number : ")
list = []
for i in number:
    list.append(int(i))
list.sort()
print("The Second Smallest digit is : ", list[1])