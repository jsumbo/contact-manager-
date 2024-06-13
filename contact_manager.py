import json
import os

# Constant for the contacts file
CONTACTS_FILE = 'contacts.json'

def load_contacts():
    """
    Load contacts from the contacts.json file.
    
    Returns:
        dict: A dictionary containing contacts data.
    """
    if not os.path.exists(CONTACTS_FILE):
        return {}
    with open(CONTACTS_FILE, 'r') as file:
        return json.load(file)

def save_contacts(contacts):
    """
    Save contacts to the contacts.json file.
    
    Args:
        contacts (dict): A dictionary containing contacts data.
    """
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    """
    Add a new contact. Prompts the user for the name, phone number, and email address.
    Performs validation and saves the contact if valid.
    """
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    
    # Validate inputs
    if not name or not phone or not email:
        print("All fields are required!")
        return
    
    contacts = load_contacts()
    
    # Check if contact already exists
    if name in contacts:
        print("Contact already exists.")
        return
    
    # Add new contact
    contacts[name] = {
        'phone': phone,
        'email': email
    }
    
    save_contacts(contacts)
    print(f"\nContact '{name}' added successfully with details:")
    print(f"  Phone: {phone}")
    print(f"  Email: {email}\n")

def view_contacts():
    """
    View all contacts. Loads the contacts from the file and displays them.
    """
    contacts = load_contacts()
    
    if not contacts:
        print("No contacts found.")
        return
    
    # Display each contact
    for name, details in contacts.items():
        print(f"  Name: {name}")
        print(f"  Phone: {details['phone']}")
        print(f"  Email: {details['email']}")
        print("-" * 20)

def delete_contact():
    """
    Delete a contact. Prompts the user for the name of the contact to delete.
    """
    name = input("Enter the name of the contact to delete: ").strip()
    
    contacts = load_contacts()
    
    # Check if contact exists
    if name not in contacts:
        print("Contact not found.")
        return
    
    # Delete contact
    del contacts[name]
    save_contacts(contacts)
    print(f"Contact '{name}' deleted successfully.")

def confirm_exit():
    """
    Confirm if the user wants to exit the application.
    
    Returns:
        bool: True if the user confirms exit, False otherwise.
    """
    while True:
        choice = input("Are you sure you want to exit? (1. Yes, 2. No): ").strip()
        if choice == '1':
            return True
        elif choice == '2':
            return False
        else:
            print("Invalid choice. Please choose 1 for Yes or 2 for No.")

def main():
    """
    Main function to display the menu and handle user choices.
    """
    print("\nWelcome to the Simple Contact Manager!")
    print("You can use this application to add, view, and delete contacts.\n")
    
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")
        
        choice = input("Choose an option: ").strip()
        
        # Handle user choices with error handling
        if choice == '1':
            try:
                add_contact()
            except Exception as e:
                print(f"An error occurred while adding contact: {e}")
        elif choice == '2':
            try:
                view_contacts()
            except Exception as e:
                print(f"An error occurred while viewing contacts: {e}")
        elif choice == '3':
            try:
                delete_contact()
            except Exception as e:
                print(f"An error occurred while deleting contact: {e}")
        elif choice == '4':
            if confirm_exit():
                print("Exiting...")
                break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
