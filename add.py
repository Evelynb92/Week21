from contact import Contacts

def set_Contacts_attribute(valid_input,counter):
    '''Takes user input for each attribute and finds match '''
    if counter == 0:
        Contacts.first_name = valid_input

    if counter == 1:
        Contacts.last_name = valid_input

    if counter == 2:
        Contacts.cellphone_number = valid_input

    if counter == 3:
        Contacts.email = valid_input

    if counter == 4:
        Contacts.home_number = valid_input


def create_contact():
    '''Takes user input and saves it in a file'''
    with open("contact library", 'a') as file:
        file.write(f"{Contacts.first_name},{Contacts.last_name},{Contacts.cellphone_number},{Contacts.email},{Contacts.home_number},\n")