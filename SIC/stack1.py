import sys as s
list = []
def add(n):
    list.append(n)
def remove():
    if len(list) == 0:
        print("Stack is empty")
    else:    
        list.pop()
    #print("Removed the element : ")
def print_list():
     if len(list) == 0:
        print("Stack is empty")
     else:   
        for i in list:
            print(i)
def exit_stack():
    s.exit()

def stack(choice):
  
    match(choice):
        case 1: 
            n=(input("Element to add :"))
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
        











