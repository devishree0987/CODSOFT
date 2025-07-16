import os

# Global list to store contacts. Each contact is a dictionary.
contacts = []

def clear_screen():
    """Clears the console screen for better readability."""
    # For Windows, use 'cls'; for macOS/Linux, use 'clear'
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    """Displays the main menu options to the user."""
    print("\n--- Contact Management System ---")
    print("1. Add New Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    print("---------------------------------")

def add_contact():
    """Allows the user to add a new contact with their details."""
    clear_screen()
    print("--- Add New Contact ---")
    name = input("Enter contact name: ").strip()
    # Basic validation to ensure name is not empty
    if not name:
        print("Contact name cannot be empty. Please try again.")
        input("Press Enter to continue...")
        return

    # Check for duplicate names (case-insensitive)
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"A contact with the name '{name}' already exists. Please use a unique name.")
            input("Press Enter to continue...")
            return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    address = input("Enter address: ").strip()

    new_contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    contacts.append(new_contact)
    print(f"\nContact '{name}' added successfully!")
    input("Press Enter to continue...")

def view_contacts():
    """Displays a list of all saved contacts with names and phone numbers."""
    clear_screen()
    print("--- Contact List ---")
    if not contacts:
        print("No contacts available. Add some contacts first!")
    else:
        # Sort contacts alphabetically by name for better readability
        sorted_contacts = sorted(contacts, key=lambda c: c['name'].lower())
        for i, contact in enumerate(sorted_contacts):
            print(f"{i+1}. Name: {contact['name']}, Phone: {contact['phone']}")
    input("Press Enter to continue...")

def search_contact():
    """Implements a search function to find contacts by name or phone number."""
    clear_screen()
    print("--- Search Contact ---")
    search_term = input("Enter name or phone number to search: ").strip().lower()
    found_contacts = []

    for contact in contacts:
        # Check if the search term is in the name or phone number (case-insensitive)
        if search_term in contact['name'].lower() or \
           search_term in contact['phone'].lower():
            found_contacts.append(contact)

    if not found_contacts:
        print(f"No contacts found matching '{search_term}'.")
    else:
        print(f"\nFound {len(found_contacts)} contact(s):")
        for i, contact in enumerate(found_contacts):
            print(f"{i+1}.")
            print(f"   Name: {contact['name']}")
            print(f"   Phone: {contact['phone']}")
            print(f"   Email: {contact['email']}")
            print(f"   Address: {contact['address']}")
            print("-" * 20) # Separator for multiple results
    input("Press Enter to continue...")

def update_contact():
    """Enables users to update contact details."""
    clear_screen()
    print("--- Update Contact ---")
    if not contacts:
        print("No contacts to update. Add some contacts first!")
        input("Press Enter to continue...")
        return

    view_contacts_for_selection() # Helper to show numbered list for selection

    try:
        choice = int(input("Enter the number of the contact to update: "))
        if 1 <= choice <= len(contacts):
            contact_to_update = contacts[choice - 1]
            print(f"\nUpdating contact: {contact_to_update['name']}")

            # Prompt for new details, allowing user to keep old value by pressing Enter
            new_name = input(f"Enter new name (current: {contact_to_update['name']}): ").strip()
            new_phone = input(f"Enter new phone (current: {contact_to_update['phone']}): ").strip()
            new_email = input(f"Enter new email (current: {contact_to_update['email']}): ").strip()
            new_address = input(f"Enter new address (current: {contact_to_update['address']}): ").strip()

            # Update only if new input is provided
            if new_name:
                contact_to_update['name'] = new_name
            if new_phone:
                contact_to_update['phone'] = new_phone
            if new_email:
                contact_to_update['email'] = new_email
            if new_address:
                contact_to_update['address'] = new_address

            print(f"\nContact '{contact_to_update['name']}' updated successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print(f"An error occurred: {e}")
    input("Press Enter to continue...")

def delete_contact():
    """Provides an option to delete a contact."""
    clear_screen()
    print("--- Delete Contact ---")
    if not contacts:
        print("No contacts to delete. Add some contacts first!")
        input("Press Enter to continue...")
        return

    view_contacts_for_selection() # Helper to show numbered list for selection

    try:
        choice = int(input("Enter the number of the contact to delete: "))
        if 1 <= choice <= len(contacts):
            deleted_contact = contacts.pop(choice - 1) # Remove the contact from the list
            print(f"\nContact '{deleted_contact['name']}' deleted successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print(f"An error occurred: {e}")
    input("Press Enter to continue...")

def view_contacts_for_selection():
    """Helper function to display contacts with numbers for selection."""
    print("\n--- Select a Contact ---")
    if not contacts:
        print("No contacts available.")
        return
    for i, contact in enumerate(contacts):
        print(f"{i+1}. Name: {contact['name']}, Phone: {contact['phone']}")
    print("------------------------")


def main():
    """Main function to run the contact management application."""
    while True:
        clear_screen()
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
            input("Press Enter to continue...")

# Entry point of the program
if __name__ == "__main__":
    main()
