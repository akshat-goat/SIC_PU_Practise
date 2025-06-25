'''
Accept the average score from the student and give her the results as follows:
0 to 69 Fail
70 to 84 Second Class
85 to 95 First Class
96 to 100 Excellent

'''


average_score = float(input("Enter Your Average Score: "))
if average_score >= 0 and  average_score <= 69 :
    print("You Have Failed")
elif  average_score <= 84 :
    print("You got Second Division ")
elif  average_score <= 95 :
    print("You've got First Class ")
elif  average_score <= 100 :
    print("You've Got EXCELLENT")
else :
    print("Invalid Input")