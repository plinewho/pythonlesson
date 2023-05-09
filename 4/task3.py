# импортируем класс
class Phonebook:
    contacts = []

    def __init__(self, fullname, tel):
        self.__fullname = fullname
        self.__tel = tel

    @property
    def fullname(self):
        return self.__fullname
    @property
    def tel(self):
        return self.__tel
   

    @classmethod
    def add_contact(cls, contact):
        cls.contacts.append(contact)

    @staticmethod
    def print_info(obj):
        print('-------------------')
        print('ФИ:', obj.fullname)
        print('Телефон:', obj.tel)
        print('-------------------')

    @classmethod
    def print_contacts(cls):
        for i in cls.contacts:
            Phonebook.print_info(i)


    def change_phone(self, tel):
        self.__tel = tel

    @classmethod
    def search_contact(cls, contact):
        for i in cls.contacts:
            if i.fullname == contact:
                print('Найденный контакт: ')
                Phonebook.print_info(i)


# создаем объекты контактов
contact1 = Phonebook("Иван Иванов", "+7 (111) 111-11-11")
contact2 = Phonebook("Петр Петров", "+7 (222) 222-22-22")

# добавляем контакт
contact3 = Phonebook("Сергей Сергеев", "+7 (333) 333-33-33")
Phonebook.add_contact(contact1)
Phonebook.add_contact(contact2)
Phonebook.add_contact(contact3)

# изменяем данные контакта
contact1.change_phone("+7 (444) 444-44-44")

# выводим информацию о всех контактах
Phonebook.print_contacts()

# ищем контакт по имени
Phonebook.search_contact("Петр Петров")