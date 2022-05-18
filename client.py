class Customers:
    def __init__(self, first_name, second_name, city, balance):
        self.first_name = first_name
        self.second_name = second_name
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'{self.first_name} {self.second_name}. {self.city}, Balance: {self.balance} руб.'
    def get_guest(self):
        return f'{self.first_name} {self.second_name}. {self.city}.'