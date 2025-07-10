def get_minimum_cost(k, costs):
 
    costs.sort(reverse=True)

    total_min_cost = 0
    n = len(costs)

  
    for i in range(n):
       
        current_multiplier = (i // k) + 1
        total_min_cost += current_multiplier * costs[i]

    return total_min_cost


print(get_minimum_cost(3, [9, 7, 5, 3, 1]))


print(get_minimum_cost(2, [10, 20, 30])) 