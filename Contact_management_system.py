import pickle

class Contact:
    def __init__(self, name, phone_number, email_address):
        self.name = name
        self.phone_number = phone_number
        self.email_address = email_address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone_number}, Email: {self.email_address}"

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contacts:")
            for contact in self.contacts:
                print(contact)

    def edit_contact(self, name, phone_number, email_address):
        for contact in self.contacts:
            if contact.name == name:
                contact.phone_number = phone_number
                contact.email_address = email_address
                print("Contact edited successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for i, contact in enumerate(self.contacts):
            if contact.name == name:
                del self.contacts[i]
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

    def save_contacts_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.contacts, file)
        print("Contacts saved successfully.")

    def load_contacts_from_file(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.contacts = pickle.load(file)
            print("Contacts loaded successfully.")
        except FileNotFoundError:
            print("No contacts file found.")
        except Exception as e:
            print(f"Error loading contacts: {e}")

def main():
    contact_manager = ContactManager()
    filename = "contacts.pkl" # File to store contacts
    
    # Load contacts from file if it exists
    contact_manager.load_contacts_from_file(filename)

    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Save Contacts")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email_address = input("Enter email address: ")
            contact_manager.add_contact(Contact(name, phone_number, email_address))
        elif choice == '2':
            contact_manager.view_contacts()
        elif choice == '3':
            name = input("Enter name of contact to edit: ")
            phone_number = input("Enter new phone number: ")
            email_address = input("Enter new email address: ")
            contact_manager.edit_contact(name, phone_number, email_address)
        elif choice == '4':
            name = input("Enter name of contact to delete: ")
            contact_manager.delete_contact(name)
        elif choice == '5':
            contact_manager.save_contacts_to_file(filename)
        elif choice == '6':
            print("Exiting...")
            # Save contacts to file before exiting
            contact_manager.save_contacts_to_file(filename)
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
