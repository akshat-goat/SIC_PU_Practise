
def bubble_sort(given_array):
    array_length = len(given_array)
    for i in range(1,array_length-1):
        check_sorted = True
        for j in range(1,array_length-1-i):
            if given_array[j] > given_array[j+1]:
                temp = given_array[j]
                given_array[j] = given_array[j+1]
                given_array[j+1] = temp
                check_sorted = False
        if sorted:
            break


def selection_sort(given_array):
    array_length = len(given_array)
    for i in range( 2, array_length):
        element = given_array[i-1]
        position = i - 1
        for j in range(i - 1,array_length):
            if given_array[j] < element:
                element = given_array[j]
                position = j
        temp = given_array[position]
        given_array[position] = given_array[i-1]   
        given_array[i-1] = temp 
        

given_array = list(map(int,input("Enter the numbers to be sorted with spaces : ").split()))
#bubble_sort(given_array)
selection_sort(given_array)
print(given_array)