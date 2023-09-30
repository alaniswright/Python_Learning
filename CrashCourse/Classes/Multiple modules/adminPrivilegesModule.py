from userModule import user

class privileges():
    def __init__(self):
        self.privileges = ["Can add post", "Can delete post", "Can ban user"]
    
    def show_privileges(self):
        print("Admin privileges: " + str(self.privileges))

class administrator(user):
    """Represents aspects of a user specific to administrators"""

    def __init__(self, first_name, last_name):
        """
        Initialise attributes of parent class
        Then initialise attributes specific to ice cream stands 
        """
        super().__init__(first_name, last_name)
        self.privileges = privileges()