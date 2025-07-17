def find_min_max(numbers_list):
    if not numbers_list:
        print("The list is empty. Cannot find smallest and biggest elements.")
        return None, None

    smallest = min(numbers_list)
    biggest = max(numbers_list)

    return smallest, biggest


print("---  Find Smallest and Biggest Elements ---")
while True:
        try:
            input_str = input("Enter numbers separated by spaces (e.g., 10 5 20 15): ")
            my_numbers = [int(x) for x in input_str.split()]
            break
        except ValueError:
            print("Invalid input. Please enter numbers separated by spaces.")

smallest_num, biggest_num = find_min_max(my_numbers)

if smallest_num is not None: # Check if the list was not empty
    print(f"Original List: {my_numbers}")
    print(f"Smallest element: {smallest_num}")
    print(f"Biggest element: {biggest_num}")

