def save_contact(contacts):
    """Takes user input and saves it in a file"""
    with open("contact library", 'a') as file:
        file.write(f"\n{contacts.first_name},{contacts.last_name},{contacts.cellphone_number},{contacts.email},{contacts.home_number},")
