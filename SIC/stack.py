import sys as s
list = []
def add(n):
    list.append(n)
def remove():
    list.pop()
    #print("Removed the element : ")
def print_list():
    for i in list:
        print(i)
def exit_stack():
    s.exit()

def stack(choice):
  
    match(choice):
        case 1: 
            n=int(input("Element to add :"))
            add(n)
        case 2: 
            remove()
        case 3: 
            print_list()
        case 4:
            exit_stack()

while True:
     print('1:Add element 2:Remove Element 3: Display Stack  4:Exit')
     choice = int(input("Enter your choice : "))
     stack(choice)
        











