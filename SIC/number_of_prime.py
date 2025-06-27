#Count the number of prime digits in a number
def prime(n):
    count=0
    for i in range (2,n+1):
        if n % i == 0 :
            count = count + 1
    if count == 1 :
        return True
    else :
        return False
#add a function to remove the copies of the prime numbers


number = input("Enter the Number : ")
digits=[]
prime_digits=[]
for i in number:
     digits.append(int(i))
for i in digits:
    if prime(i) == True:
        prime_digits.append(int(i))
print("Number of prime digits = ",len(prime_digits))

