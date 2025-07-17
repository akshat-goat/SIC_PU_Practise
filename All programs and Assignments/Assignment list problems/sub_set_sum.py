def is_subset_sum(numbers, target_sum):
    n = len(numbers)

    def backtrack(index, current_sum):
        # Base cases
        if current_sum == target_sum:
            return True
        if current_sum > target_sum or index == n:
            return False
        
        # Recursive calls:
        # 1. Include the current number (numbers[index])
        if backtrack(index + 1, current_sum + numbers[index]):
            return True
        
        # 2. Exclude the current number (numbers[index])
        if backtrack(index + 1, current_sum):
            return True
        
        return False

    return backtrack(0, 0)

if __name__ == "__main__":
    print("--- Subset Sum Problem ---")
    
    while True:
        try:
            input_nums_str = input("Enter numbers (space-separated): ")
            nums = list(map(int, input_nums_str.split()))
            break
        except ValueError:
            print("Invalid input. Please enter integers separated by spaces.")
            
    while True:
        try:
            target = int(input("Enter the target sum: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer for the target sum.")

    if is_subset_sum(nums, target):
        print(f"A subset with sum {target} exists in {nums}.")
    else:
        print(f"No subset with sum {target} exists in {nums}.")