from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        self.value = value.strip()

    def value(self):
        return self._value()

class Phone(Field):
    def __init__(self, value):
        self._validate_phone(value)
        super().__init__(value)

    def _validate_phone(self, phone):
        if not phone.isdigit():
            raise ValueError(f"Phone number must contain only digits. Provided: {phone}")
        if len(phone) != 10:
            raise ValueError(f"Phone number must contain exactly 10 digits. Provided: {phone}")

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        phone_to_remove = None
        for p in self.phones:
            if p.value == phone:
                phone_to_remove = p
                break
        if phone_to_remove:
            self.phones.remove(phone_to_remove)
        else:
            raise ValueError(f"Phone {phone} not found.")

    def edit_phone(self, old_phone, new_phone):
        phone_to_edit = None
        for p in self.phones:
            if p.value == old_phone:
                phone_to_edit = p
                break
        if phone_to_edit:
            if old_phone == new_phone:
                raise ValueError("New phone number cannot be the same as the old one.")
            if not new_phone.isdigit():
                raise ValueError(f"Phone number must contain only digits. Provided: {new_phone}")
            if len(new_phone) != 10:
                raise ValueError(f"Phone number must contain exactly 10 digits. Provided: {new_phone}")
            phone_to_edit.value = new_phone
        else:
            raise ValueError(f"Phone {old_phone} not found.")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)
        
    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError(f"Record with name '{name}' not found.")
    
    def __str__(self):
        if not self.data:
            return "Address Book is empty."

        result = []
        for record in self.data.values():
            phones = ', '.join(phone.value for phone in record.phones) if record.phones else "No phones"
            result.append(f"Name: {record.name.value}, Phones: {phones}")
        
        return "\n".join(result)
    

# book = AddressBook()

# john_record = Record("John")
# john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")

# # Додавання запису John до адресної книги
# book.add_record(john_record)

# # Створення та додавання нового запису для Jane
# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")
# book.add_record(jane_record)

# # Виведення всіх записів у книзі
     
# print(book)

# # Знаходження та редагування телефону для John
# john = book.find("John")
# john.edit_phone("1234567890", "1112223333")

# print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# # Пошук конкретного телефону у записі John
# found_phone = john.find_phone("5555555555")
# print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

# # Видалення запису Jane
# book.delete("Jane")
