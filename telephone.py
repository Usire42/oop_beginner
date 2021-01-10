
class Phone:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.contacts = {}

    def add_contact (self, new_name, new_number):
        new_name = self.user_input(new_name)
        new_number = self.user_input(new_number)
        if (self.search_contact(new_name) or self.search_contact(new_number)) == False:
            self.contacts.update({new_name: new_number})
        else:
            input_ = input(f'Would you like add new number to contact {new_name}? Y/N - ').lower()
            if input_ == "n":
                return "Number wasn't add to contact."
            else:
                contact_numbers = list(self.contacts.get(new_name, new_number))
                contact_numbers.append(new_number)
                self.contacts.update({new_name: contact_numbers})
                return f'Number {new_number} was added to contact {new_name}'

    def search_contact(self, key):
        for name, number in self.contacts.items():
            if name == key:
                return f'{name}: {number}'
            elif number in key:
                return f'{name}: {number}'
        else:
            return False

    def user_input(self, input_):
        return f"{input_}"

    def delete_contact (self, key):
        del_cont = self.search_contact(key)
        if del_cont == False:
            return f"{key} doesn't exist"


phone = Phone('a', 'b')
phone.add_contact('ahoj', '555555555')
print(phone.contacts)
phone.add_contact('Nee', '555555555')
print(phone.contacts)
phone.add_contact('ahoj', '666666666')

print(phone.contacts)



