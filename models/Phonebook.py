
from models.Contact import Contact

class Phonebook():
    def __init__(self) -> None:
        self.contacts: list[Contact] = []

    def insert_contact(self, contact):
        self.contacts.append(contact)

    def get_contact_by_name(self, name):
        return list(filter(lambda contact: name in contact.name, self.contacts))
    
    def get_contact_by_phone(self, phone):
        return list(filter(lambda contact: phone in contact.phone, self.contacts))
    
    def __get_contacts_by_field(self, value, type):
        if type == "Name":
            return self.get_contact_by_name(value)
        else:
            return self. get_contact_by_phone(value)
        
    def get_all_contacts(self):
        return self.contacts
