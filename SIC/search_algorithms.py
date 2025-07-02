

def linear_search(array_to_be_searched_from , number_to_be_searched):
    found = False   
    for i in array_to_be_searched_from:
        if i == number_to_be_searched:
            found = True
    if found == True:
        print("Number is found !")
    else :
        print("Number is not in the given list.")

def binary_search(array_to_be_searched_from ,number_to_be_searched ):
    left_most_index = 0
    right_most_index = len(array_to_be_searched_from)-1
    found = False
    while left_most_index <= right_most_index :
        middle_index = (left_most_index + right_most_index) // 2
        if array_to_be_searched_from[middle_index] == number_to_be_searched :
            found = True
        elif number_to_be_searched < array_to_be_searched_from[middle_index]:
            right_most_index = middle_index - 1
        else :
            left_most_index = middle_index + 1
    if found == True:
        print("Number is found !")
    else :
        print("Number is not in the given list.") 


array_to_be_searched_from = list(map(int,input("Enter the array : ").split()))
number_to_be_searched = int(input("Enter the number you want to search for : "))
linear_search(array_to_be_searched_from , number_to_be_searched)
binary_search(array_to_be_searched_from   , number_to_be_searched)