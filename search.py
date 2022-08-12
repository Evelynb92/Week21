from contact import Contacts


def contact_searched(user_input):
    """Takes in 1st & last name user is searching for and returns user info"""
    with open("contact library", "r") as file:
        data = file.read().splitlines()

    # create an empty contact
    found_contact = Contacts()

    # for each line in the data pulled from the contact library.
    for contact_info in data:
        print(contact_info)
        if contact_info.split(',')[0] == user_input:
            found_contact.first_name = contact_info.split(',')[0]
            found_contact.last_name = contact_info.split(',')[1]
            found_contact.cellphone_number = contact_info.split(',')[2]
            found_contact.email = contact_info.split(',')[3]
            found_contact.home_number = contact_info.split(',')[4]
            return found_contact
        else:
            found_contact.first_name = 'NOT FOUND'
            found_contact.last_name = 'NOT FOUND'
            found_contact.cellphone_number = 'NOT FOUND'
            found_contact.email = 'NOT FOUND'
            found_contact.home_number = 'NOT FOUND'
    return found_contact


