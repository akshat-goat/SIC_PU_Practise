def partition_palindromes(s):

    results = []
    
    def is_palindrome(sub):
        return sub == sub[::-1]

    def backtrack(start_index, current_partition):
        if start_index == len(s):
            results.append(list(current_partition))
            return

        for i in range(start_index, len(s)):
            substring = s[start_index : i + 1]
            if is_palindrome(substring):
                current_partition.append(substring)
                backtrack(i + 1, current_partition)
                current_partition.pop() # Backtrack

    backtrack(0, [])
    return results

if __name__ == "__main__":
    print("--- Palindrome Partitioning ---")
    input_str = input("Enter a string: ")
    if not input_str:
        print("Input string cannot be empty.")
    else:
        partitions = partition_palindromes(input_str)
        print(f"All palindrome partitions of '{input_str}':")
        print(partitions)
