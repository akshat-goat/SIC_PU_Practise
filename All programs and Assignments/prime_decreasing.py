#check if the given number is prime 
def is_prime(n):
    if n == 0 or n == 1:
        return False
    elif n == 2 :
        return True
    else :
        count = 0
        for i in range (2,n+1):
            if n % i == 0 :
                count = count + 1
        if count == 1 :
            return True
        else :
            return False
while True:      
    m = int(input("Enter the Range (m): "))
    
    n = int(input("Enter the Range (n): "))
    if m > n:
        break
    else :
        print("Enter m and n such that M is greater than n")

for i in range(m,n,-1):
    if is_prime(i) == True:
        print(i)
    
