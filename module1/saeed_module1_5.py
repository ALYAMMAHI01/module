# module1/saeed_module1_5.py
# This module provides a function to shift letters in a string,
# count words, and calculate the price based on letter count.
# Each letter is shifted to the next letter in the alphabet,
# with 'z' wrapping around to 'a' and 'Z' to 'A'.
# Non-letter characters remain unchanged.
# The function also counts the number of words and calculates
# the total price based on a given price per letter.
def shift_string_and_calculate(string, price_per_letter):
    def shift_letter(c):
        if c.islower():
            return chr((ord(c) - ord('a') + 1) % 26 + ord('a'))
        elif c.isupper():
            return chr((ord(c) - ord('A') + 1) % 26 + ord('A'))
        else:
            return c
    
    shifted = ''.join(shift_letter(c) for c in string)
    words = string.split()
    word_count = len(words)
    letter_count = sum(1 for c in string if c.isalpha())
    price_of_string = letter_count * price_per_letter
    
    return {
        "shifted_string": shifted,
        "word_count": word_count,
        "price_of_string": price_of_string
    }

# Example usage
if __name__ == "__main__":
    result = shift_string_and_calculate("Hello World", 0.5)
    print(result)


# Example output:# {
#     "shifted_string": "Ifmmp Xpsme",
#     "word_count": 2,
#     "price_of_string": 5.0

#note: The example output is provided as a comment for clarity and is not part of the executable code.