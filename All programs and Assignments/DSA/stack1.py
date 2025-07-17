#a Stack using a list, where elements are inserted and deleted from the rear of the list.
import sys as s
my_stack = []
def push(n):
    my_stack.append(n)

def pop():
    if len(my_stack) == 0:
        print("Stack is empty")
    else:    
        my_stack.pop()
    #print("Removed the element : ")

def display():
     if len(my_stack) == 0:
        print("Stack is empty")
     else:   
        for i in my_stack:
            print(i)

def exit():
    s.exit()

def stack(choice):
  
    match(choice):
        case 1: 
            n=(input("Element to add :"))
            push(n)
        case 2: 
            pop()
        case 3: 
            display()
        case 4:
            exit()

while True:
     print('1:Add element 2:Remove Element 3: Display Stack  4:Exit')
     choice = int(input("Enter your choice : "))
     stack(choice)
        











