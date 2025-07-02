
k = 0
number_of_oranges_plucked = int(input())
diameters_of_oranges_plucked = list(map(int, input().split()))
pivot = diameters_of_oranges_plucked[number_of_oranges_plucked - 1]

for i in range(number_of_oranges_plucked - 1):
    if diameters_of_oranges_plucked[i] <= pivot:
        
        diameters_of_oranges_plucked[i], diameters_of_oranges_plucked[k] = diameters_of_oranges_plucked[k], diameters_of_oranges_plucked[i]
        k += 1

diameters_of_oranges_plucked[k], diameters_of_oranges_plucked[number_of_oranges_plucked - 1] = diameters_of_oranges_plucked[number_of_oranges_plucked - 1], diameters_of_oranges_plucked[k]

print(diameters_of_oranges_plucked)
