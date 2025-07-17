def generate_permutations(s):

    if len(s) <= 1:
        return [s]
    
    permutations = []
    # Iterate through each character in the string
    for i, char in enumerate(s):
        # Remaining characters after picking 'char'
        remaining_chars = s[:i] + s[i+1:]
        
        # Get permutations of the remaining characters
        for perm in generate_permutations(remaining_chars):
            permutations.append(char + perm)
            
    return list(set(permutations)) # Use set to handle unique permutations if input string has duplicates

if __name__ == "__main__":
    print("--- Permutations of a String ---")
    input_str = input("Enter a string: ")
    if not input_str:
        print("Input string cannot be empty.")
    else:
        all_perms = generate_permutations(input_str)
        print(f"All permutations of '{input_str}':")
        print(all_perms)
