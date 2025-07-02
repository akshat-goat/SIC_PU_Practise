
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
        
def partition(array, low, high):
    pivot = array[high]
    k = low -1
    for i in range(low, high):
        if array[i] <= pivot:
            k += 1
            array[i], array[k] = array[k], array[i]
    array[k+1], array[high] = array[high], array[k+1]
    return k+1


def quick_sort(array, low, high):

    if low < high:
        pivot_index = partition(array, low, high)
        quick_sort(array, low, pivot_index-1)
        quick_sort(array, pivot_index + 1, high)

given_array = list(map(int,input("Enter the numbers to be sorted with spaces : ").split()))
#bubble_sort(given_array)
#selection_sort(given_array)
low_index = 0
high_index = len(given_array)-1
quick_sort(given_array, low_index, high_index)
print(given_array)