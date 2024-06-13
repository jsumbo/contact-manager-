# Contact Manager

## Project Aim

I did this project to practice my data structures skills in Python, specifically focusing on lists. The goal is to build a command-line application for storing and managing contacts. The application allows users to add, view, and delete contacts with proper error handling.

## Features

- **Add Contact**: Add a new contact by entering a name, phone number, and email address.
- **View Contacts**: View all stored contacts.
- **Delete Contact**: Delete a contact by entering the contact's name.
- **Exit Confirmation**: Confirm before exiting the application.

### Code Structure

- `load_contacts()`: Loads contacts from the JSON file.
- `save_contacts()`: Saves contacts to the JSON file.
- `add_contact()`: Adds a new contact.
- `view_contacts()`: Displays all contacts.
- `delete_contact()`: Deletes a specified contact.
- `confirm_exit()`: Confirms before exiting the application.
- `main()`: Main function to handle user input and run the application.

## Technologies Used

- Python
- JSON (for storing contacts)

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository or download the `contact_manager.py` file.
2. Ensure Python is installed on your system.

### Usage

1. Open a terminal or command prompt.
2. Navigate to the directory where `contact_manager.py` is located.
3. Run the script using Python:

    ```sh
    python3 contact_manager.py
    ```

4. Follow the on-screen instructions to add, view, or delete contacts.

## Error Handling

The application includes error handling to manage common issues such as invalid input, file access errors, and duplicate contacts.
