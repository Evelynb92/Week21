def save_contact(contacts):
    '''Takes user input and saves it in a file'''
    with open("contact library", 'a') as file:
        file.write(f"{Contacts.first_name},{Contacts.last_name},{Contacts.cellphone_number},{Contacts.email},{Contacts.home_number},\n")