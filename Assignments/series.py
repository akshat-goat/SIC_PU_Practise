power=1
denominator = 1
while True:
    n = int(input("Give the Value for n (1<=n<=4):"))
    if 1 <= n <= 4 :
        break
    else:
        print("Invalid Input .Enter Value between 1 and 4")
        
while True:
    m = int(input ("Give range (m) {Should be between 1 and 10}:"))
    if 2 <= m <= 10:
        break
    else:
        print("Invalid Input . Enter a Value Between 2 And 10")
sum_of_series = 0
sign = 1
for _ in range(m):
    term = sign *(n ** power) / denominator 
    sum_of_series += term
    power = power * 2
    denominator = denominator + 2
    sign *= -1
print("THe sum of the series = ",sum_of_series)