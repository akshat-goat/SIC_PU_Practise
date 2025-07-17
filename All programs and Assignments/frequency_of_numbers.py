def check_frequency( my_list, element):
    frequency = my_list.count(element)
    return frequency

def remove_duplicates(data_list):
    seen = set()
    unique_list = []
    for item in data_list:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    return unique_list


#while True:
input_list = input("Enter Numbers with spaces (i.e.  2 43 11 44 : )")
my_list = input_list.split()

my_list1 = remove_duplicates(my_list)


for i in my_list1:
    print(f"{i} occurs {check_frequency(my_list,i)}")
