class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'{self.name} {self.surname}. {self.city}. Banalce: {self.balance}.'

    def get_main_info(self):
        return f'{self.name} {self.surname}, {self.city}'


client1 = Client('Ivan', 'Petrov', 'SPb', 150)
client2 = Client('Boris', 'Ivanov', 'Moscow', 320)
client3 = Client('Alex', 'Sidorov', 'Tomsk', 1560)
print(client1)

client_list = [client1, client2, client3]
for client in client_list:
    print(client.get_main_info())
