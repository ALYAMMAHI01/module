# Function to read address from a file, count the words, and append the count back to the file
# The file is expected to have a line starting with "Address: "

def read_address_and_count_words(filename="person_address.txt"):
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
        
        address_text = ""
        for line in lines:
            if line.startswith("Address: "):
                address_text = line[len("Address: "):].strip()
                break
        
        if not address_text:
            return None
        
        word_count = len(address_text.split())
        
        # Append the word count to the file
        with open(filename, 'a') as f:
            f.write(f"\nWord count of address: {word_count}\n")
        
        return word_count
    except FileNotFoundError:
        print(f"File {filename} not found.")
        return None

# Example usage
if __name__ == "__main__":
    word_count = read_address_and_count_words()
    if word_count is not None:
        print(f"Word count appended: {word_count}")



# nb: This function reads a file named "person_address.txt", looks for a line starting with "Address: ",
# counts the number of words in that address, and appends the word count back to the
# same file. If the file does not exist, it handles the FileNotFoundError gracefully.
# The function returns the word count if successful, or None if the address line is not found or the file is missing.


#note: Make sure to create a file named "person_address.txt" with an appropriate address line for testing.