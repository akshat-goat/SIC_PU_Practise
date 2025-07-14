"""
scores = [100, 90, 95, 90, 80, 70, 0, 80, 90, 0, 90, 100, 75, 20, 30, 50, 90]
valid_scores =[]
total_students = len(scores) / 3
for i in scores:
    if i != 0 :
        valid_scores.append(i)
students_with_valid_scores = len(valid_scores) / 3
print(scores)
print(f"The number of total students is {total_students}")
print(f"The number of total students is {students_with_valid_scores}")
print(valid_scores)
"""

scores=[100, 90, 95,90,80,70,0,80,90,90,0,90,100,75,20,30,50,90]
last_idx=3
strt_idx=0
main_list=[]
count_of_valid_students=0
while last_idx<=len(scores):
    temp_list=scores[strt_idx:last_idx]
    strt_idx+=3
    last_idx+=3
    if 0 not in temp_list:
        main_list.append(temp_list)
        count_of_valid_students  += 1
print(main_list)
print("total valid students are:",count_of_valid_students)