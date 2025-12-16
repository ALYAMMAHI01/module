
# This module defines a Person class that stores personal information
# and provides a method to save that information to a text file
# including name, contact, address, and phone number.
class Person:
    def __init__(self, name, contact, address, phone):
        self.name = name
        self.contact = contact
        self.address = address
        self.phone = phone
    
    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(f"Name: {self.name}\n")
            f.write(f"Contact: {self.contact}\n")
            f.write(f"Address: {self.address}\n")
            f.write(f"Phone: {self.phone}\n")
        print(f"Person's information saved to {filename}")

# Example usage
if __name__ == "__main__":
    name = input("Enter name: ")
    contact = input("Enter contact: ")
    address = input("Enter address: ")
    phone = input("Enter phone number: ")
    
    person = Person(name, contact, address, phone)
    person.save_to_file("person_address.txt")
