from models.Contact import Contact
from models.Phonebook import Phonebook

itay = Contact(ID="111111111", name="Itay shapira",phone="+972544391936", email="itay@efsdfs.com")
guy = Contact(ID="222222222", name="Guy Taggar",phone="054-2252233", email="guy@tagfat.com")
shay = Contact(ID="333333333", name="Shay Taggar",phone="054-6666666", email="shay@gdfgdg.com")
phonebook = Phonebook()
phonebook.insert_contact(itay)
phonebook.insert_contact(guy)
phonebook.insert_contact(shay)


