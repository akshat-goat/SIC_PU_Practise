def is_rotation(original: str, rotated: str) :
    if len(original) != len(rotated):
        return False

    combined = rotated + rotated
    return original in combined



original_word = input("Enter the original word: ").strip().lower()
rotated_word = input("Enter the rotated word: ").strip().lower()

if is_rotation(original_word, rotated_word):
    print("The given string is a rotation of the original string.")
else:
    print("It is not a rotation of the original string.")