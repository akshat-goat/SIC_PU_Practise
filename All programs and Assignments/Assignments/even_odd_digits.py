def sum_even_placed_digits(number):
    """
    Sum of digits at even places (counting from right, 1-based index)
    Example: 123456 -> digits at even places: 5, 3, 1 => sum = 9
    """
    number = str(number)[::-1]
    total = 0
    for i in range(1, len(number), 2):  # Even place (index 1, 3, 5,... from right)
        total += int(number[i])
    return total

def sum_odd_placed_even_digits(number):
    """
    Sum of even digits at odd places (from right, 1-based)
    Example: 123456 -> digits at odd places: 6, 4, 2 => only 6, 4, 2 are even => sum = 12
    """
    number = str(number)[::-1]
    total = 0
    for i in range(0, len(number), 2):  # Odd place (index 0, 2, 4,... from right)
        digit = int(number[i])
        if digit % 2 == 0:
            total += digit
    return total

# --- Variations ---

def sum_even_index_digits(number):
    """
    Variation 1: Sum of digits at even indices (0-based index from left)
    Example: 123456 -> indices 0,2,4 = 1+3+5 = 9
    """
    number = str(number)
    total = 0
    for i in range(0, len(number), 2):
        total += int(number[i])
    return total

def count_even_digits_at_odd_positions(number):
    """
    Variation 2: Count even digits at odd indices (0-based index from left)
    Example: 123456 -> indices 1,3,5 = digits 2, 4, 6 -> all even => count = 3
    """
    number = str(number)
    count = 0
    for i in range(1, len(number), 2):
        if int(number[i]) % 2 == 0:
            count += 1
    return count

# --- Main ---
num = int(input("Enter the number array : "))
print("\n8. Sum of Even Placed Digits (from right):", sum_even_placed_digits(num))
print("9. Sum of Odd Placed Even Digits (from right):", sum_odd_placed_even_digits(num))

print("\nVariation 1: Sum of Digits at Even Indices (from left):", sum_even_index_digits(num))
print("Variation 2: Count of Even Digits at Odd Indices (from left):", count_even_digits_at_odd_positions(num))
