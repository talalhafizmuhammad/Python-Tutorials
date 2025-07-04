contacts = []

def add(name, phone):
    contacts.append({'name': name, 'phone': phone})
    print('Contact Added!')

def show():
    if not contacts:
        print('No contact found!')
    else:
        for i, contact in enumerate(contacts):
            print(f"{i + 1}. Name: {contact['name']}, Phone No: {contact['phone']}")

def search(name):
    found = False
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"Found! Name: {contact['name']}, Phone: {contact['phone']}")
            found = True
            break
    if not found:
                print("Contact not found!")

def update(name):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            newName = input("Enter new name: ")
            newPhone = input("Enter new Ph. No: ")
            contact['name'] = newName
            contact['phone'] = newPhone
            print('Contact Updated!')
            return
    print('Contact Not Found!')

def delete(name):
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contacts.remove(contact)
            print('Contact Deleted!')
            return
    print("Contact Not Found!")    
    
while True:
    print("\nCOntact Book")
    print('='*15)
    print('1. Add contact') 
    print('2. Show all contact')
    print('3. Search contact')
    print('4. Update contact')
    print('5. Delete contact')
    print('6. Exit')   
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        name = input('Enter name: ')
        phone = input('Enter phone: ')
        add(name, phone)
    elif choice == 2:
        show()
    elif choice == 3:
        name = input("Enter the name to search: ")
        search(name)
    elif choice == 4:
        name = input("Enter the name to update: ")
        update(name)
    elif choice == 5:
        name = input("Enter the name to delete: ")
        delete(name)
    elif choice == 6:
        print('GoodBye')
        exit()
    else:
        print("invalid choice!")
