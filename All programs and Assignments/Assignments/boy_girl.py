import sys as s
number_of_boys = int(input("Enter the number of boys : "))
number_of_girls = int(input("Enter the number of girls : "))

if number_of_boys != number_of_girls:
    s.exit("Numbers of boys and girls should be equal ")

height_of_boys = list(map(int,input("Enter height of boys :").split())).sort()
height_of_boys = list(map(int,input("Enter height of boys :").split())).sort()

