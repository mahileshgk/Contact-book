
import json
import os

FILE_NAME = "contacts.json"


# Load contacts from JSON file
def load_contacts():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            contacts = json.load(file)

            if isinstance(contacts, list):
                return contacts

            return []

    except (json.JSONDecodeError, OSError):
        print("Contact file is missing or damaged. Starting empty.")
        return []


# Save contacts to JSON file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


# Add a new contact
def add_contact(contacts):
    print("\n--- Add Contact ---")

    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    if not name or not phone:
        print("Name and phone number are required!")
        return

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    save_contacts(contacts)

    print("Contact added successfully!")


# Display all contacts
def list_contacts(contacts):
    print("\n--- Contact List ---")

    if not contacts:
        print("No contacts available.")
        return

    for i, contact in enumerate(contacts, start=1):
        print(f"\nContact {i}")
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])


# Search contacts by partial name
def search_contact(contacts):
    print("\n--- Search Contact ---")

    search_name = input("Enter name to search: ").strip().lower()

    if not search_name:
        print("Please enter a name to search.")
        return

    found = []

    for contact in contacts:
        if search_name in contact["name"].lower():
            found.append(contact)

    if not found:
        print("No matching contacts found.")
    else:
        for contact in found:
            print("\nName:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])


# Edit an existing contact
def edit_contact(contacts):
    list_contacts(contacts)

    if not contacts:
        return

    try:
        number = int(input("\nEnter contact number to edit: "))

        if number < 1 or number > len(contacts):
            print("Invalid contact number!")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    contact = contacts[number - 1]

    print("Leave a field empty to keep its old value.")

    name = input("Enter new name: ").strip()
    phone = input("Enter new phone: ").strip()
    email = input("Enter new email: ").strip()

    if name:
        contact["name"] = name

    if phone:
        contact["phone"] = phone

    if email:
        contact["email"] = email

    save_contacts(contacts)

    print("Contact updated successfully!")


# Delete a contact
def delete_contact(contacts):
    list_contacts(contacts)

    if not contacts:
        return

    try:
        number = int(input("\nEnter contact number to delete: "))

        if number < 1 or number > len(contacts):
            print("Invalid contact number!")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    removed = contacts.pop(number - 1)

    save_contacts(contacts)

    print(removed["name"], "deleted successfully!")


# Main program
def main():
    contacts = load_contacts()

    while True:
        print("\n===== CONTACT BOOK =====")
        print("1. Add Contact")
        print("2. List Contacts")
        print("3. Search Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            list_contacts(contacts)

        elif choice == "3":
            search_contact(contacts)

        elif choice == "4":
            edit_contact(contacts)

        elif choice == "5":
            delete_contact(contacts)

        elif choice == "6":
            print("Thank you for using Contact Book!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()
