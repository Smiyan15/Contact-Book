import json
FILE_NAME = "contacts.json"

#----------------load and save functions-------------------

def load_contacts():
    try:
        with open(FILE_NAME, "r") as contacts_file:
            return json.load(contacts_file)

    except FileNotFoundError:
        return []


def save_contacts(contacts):
    with open(FILE_NAME, "w") as contacts_file:
        json.dump(contacts, contacts_file, indent=4)


def add_contact(contacts):
    name= input("Enter Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    email = input("Enter Email: ").strip()


    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print(f"\nContact {name} Added Successfully!\n")


def view_contacts(contacts):
    if not contacts:
        print("There are no contacts added.\n")
        return
    print("--------------CONTACT LIST-------------------")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}.name: {contact['name']}, phone: {contact['phone']}, email: {contact['email']}")
    print("--------------------------------------------------------------------------------------")


def search_contact(contacts):
    name = input("Enter the name to search for:").strip().lower()
    found = False
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("Contact Found:\n")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            found = True
            break
    if not found:
        print("Contact not found!\n")

def update_contact(contacts):
    name = input("Enter the new name to update:").strip().lower()
    found = False
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("What do you want to update?\n")
            print("1.Name\n 2.Phone\n 3.Email")
            choice = input("Enter your choice(1-3):")

            if choice == "1":
                contact["name"]= input("Enter new name to update:").strip()
            elif choice == "2":
                contact["phone"]= input("Enter new phone number to update:").strip()
            elif choice == "3":
                contact["email"]= input("Enter new email to update:").strip()
            else:
                print("Invalid choice, please enter a number(1-3).\n")
                return

    print(f"Contact '{name}' not found")

def delete_contact(contacts):
    name = input("Enter name to delete:").strip().lower()
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            save_contacts(contacts)
            print(f"Contact '{name} deleted!\n")
            return

    print(f'contact {name} not found.\n')


def main():
    contacts = load_contacts()

    while True:
        print("==========Contact Book===============")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice(1-3):")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("\nExiting Contact Book\n")
            break
        else:
            print("Invalid choice, please enter a number(1-6).\n")



if __name__ == "__main__":
    main()

