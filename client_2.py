from client import Customers

cl_1 = Customers('Иван', 'Петров', 'Москва', 50)
cl_2 = Customers('Мария', 'Лосева', 'Астрахань', 30)
guest_list = [cl_1, cl_2]
for guest in guest_list:
    print(guest.get_guest())