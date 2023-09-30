class user:
    "A model of a user"

    def __init__(self, first_name, last_name):
        "Initialise name and last name attributes"
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    
    def describe_user(self):
        """A method that prints the users name"""
        print(self.first_name.title() + " " + self.last_name.title())
    
    def greet_user(self):
        """A method that prints a welcome message for the user"""
        print("Welcome " + self.first_name.title())
    
    def increment_login_attempts(self):
        self.login_attempts += 1
        print("Login attempts: " + str(self.login_attempts))
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        print("Login attempts: " + str(self.login_attempts))