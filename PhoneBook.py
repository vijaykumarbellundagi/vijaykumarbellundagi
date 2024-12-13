# PhoneBook
def display_menu():
    print("\nPhoneBook menu")
    print("1.Add a new contact")
    print("2.Search for a contact")
    print("3.Update a contact's phone number")
    print("4.Delete a contact")
    print("5.List of all contact")
    print("6.Exit")

def add_contact(phonebook):
    name=input("Enter the contect name")
    if (name in phonebook):
        print(f"{name} already exists!! in your phonebook with number {phonebook[name]}")
    else:
        phone=input("Enter phone number")
        phonebook[name]=phone
        print(f"Contact {name} added successfully")

def search_contact(phonebook):
    name=input("Enter the contact name to search")
    if name in phonebook:
        print(f"Contact {name} found with phone number {phonebook[name]}")
    else:
        print(f"Contact {name} not found!!")      

def update_contact(phonebook):
    name=input("Enter the contact name to update")
    if name in phonebook:
        new_phone=input(f"Enter the new phone number {name}")
        phonebook[name]=new_phone
        print(f"Contact {name} updated successfully")
    else:
        print(f"Contact {name} not found!!")

def delete_contact(phonebook):
    name=input("Enter the contact name to delete")
    if name in phonebook:
        del phonebook[name]
        print(f"Contact {name} deleted successfully")
    else:
        print(f"Contact {name} not found!!")

def list_contact(phonebook):
    if phonebook:
        for name,phone in phonebook.items():
            print(f"{name}:{phone}")
    else:
        print("No contacts in your phonebook!!")
            
def main():
    phonebook={}
    while(True):
        display_menu()
        choice=input("Enter your choioce")

        if choice == "1":
            add_contact(phonebook)

        elif choice == "2":
            search_contact(phonebook)

        elif choice == "3":
            update_contact(phonebook)
        
        elif choice == "4":
            delete_contact(phonebook)

        elif choice == "5":
            list_contact(phonebook)

        elif choice == "6":
            print("Exiting the phonebook.goodbye")
            break

main()

# 

