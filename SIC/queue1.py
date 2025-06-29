#Implement Queue using list, insert at rear delete from front the list
import sys as s
my_queue = []
def enqueue(n):
    my_queue.append(n)
    print(f"Enqueued: {n}")

def is_empty():
    if len(my_queue) == 0:
        print("Stack is empty")

def dequeue():
    if is_empty():
         print("Queue is empty. Cannot dequeue.")
    else:
        a=my_queue.pop(0)
        print("Removed the element : ",a)

def peek():
     if is_empty():
        print("Queue is empty. No item to peek.")
        return None
     return my_queue[0]

def size():
    return len(my_queue)


def display():
     if len(my_queue) == 0:
        print("Stack is empty")
     else:   
        for i in my_queue:
            print(i)

def exit():
    s.exit()

def stack(choice):
  
    match(choice):
        case 1: 
            n=(input("Element to add :"))
            enqueue(n)
        case 2: 
            dequeue()
        case 3: 
            print(peek())
        case 4:
            display()
        case 5:
            exit()

while True:
     print('1:Enqueue 2:Dequeue 3: peek 4:Display 5:Exit')
     choice = int(input("Enter your choice : "))
     stack(choice)
        













