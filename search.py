class Search:

    def contact_searched(self, user_input):
        '''Takes in 1st & last name user is searching for and returns user info'''
        with open("contact library.txt", "r") as file:
            data = file.readlines()

        for contact_info in data:
            self.first_name = contact_info.split(',')[0]
            self.last_name = contact_info.split(',')[1]
            self.cellphone_number = contact_info.split(',')[2]
            self.email = contact_info.split(',')[3]
            self.home_number = contact_info.split(',')[4]

        if user_input == self.first_name:
            return True
        else:
            return False
