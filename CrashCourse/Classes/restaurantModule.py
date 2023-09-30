class restaurant:
    """A simple attempt to model a restaurant"""

    def __init__(self, name, cuisine):
        """Initialise name and cuisine attributes"""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        """Print a statement describing the restaurant"""
        print(self.name + " restaurant selling " + self.cuisine + ". Number served: " + str(self.number_served))
    
    def open_restaurant(self):
        """Print a statement stating that the restaurant is open for business"""
        print(self.name + " is open for business")
    
    def set_number_served(self, new_num_served):
        """Set the number_served value to any value"""
        self.number_served = new_num_served
    
    def increment_number_served(self):
        """Add 1 to the number of users served"""
        self.number_served += 1