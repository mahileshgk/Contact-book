# Contact Book

## Project Description
Contact Book is a simple menu-driven Python application used to manage personal contacts. It allows users to add, view, search, edit, and delete contact details. All contact information is stored in a JSON file so that the data remains available even after restarting the program.

## Features
- Add new contacts.
- Display all saved contacts.
- Search contacts using part of a name.
- Edit existing contact details.
- Delete contacts.
- Store contact information in a JSON file.
- Automatically starts with an empty contact list if the JSON file is missing or corrupted.
- Saves changes automatically.

## Technologies Used
- Python 3
- JSON Module
- OS Module

## Project Structure

```text
Contact_Book/
│
├── contact_book.py
├── contacts.json
└── README.md
```

## How to Run the Project

1. Download or clone this repository.
2. Open the Contact_Book folder in VS Code.
3. Open the terminal.
4. Run the following command:

```bash
python contact_book.py
```

## Menu Options

1. Add Contact
2. List Contacts
3. Search Contact
4. Edit Contact
5. Delete Contact
6. Exit

## Sample Contact

```json
{
    "name": "Arun",
    "phone": "9876543210",
    "email": "arun@gmail.com"
}
```

## Data Storage
The application automatically creates a `contacts.json` file to store contact information. Changes are saved automatically whenever contacts are added, edited, or deleted.

## Conclusion
This project demonstrates basic Python programming concepts such as functions, lists, dictionaries, loops, conditional statements, exception handling, and JSON file handling.

## Author
Kishore Kumar R

**Project:** Contact Book  
**Programming Language:** Python
