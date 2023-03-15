from fastapi import FastAPI
from models.Phonebook import Phonebook 
from models.Contact import Contact
import notebookApp

class Api_app():
    def __init__(self) -> None:
        self.phonebook = Phonebook()
        

app = FastAPI()

@app.get("/")
async def get_all_contact():
    return notebookApp.phonebook.get_all_contacts()

@app.get("/get_contact_by_name/{name}")
async def get_contact_by_name(name):
    return notebookApp.phonebook.get_contact_by_name(name)

@app.get("/get_contact_by_phone/{phone}")
async def get_contact_by_phone(phone):
    return notebookApp.phonebook.get_contact_by_phone(phone)

@app.post("/add_contact", status_code=201)
async def add_contact(contact: Contact):
    notebookApp.phonebook.insert_contact(contact)
    return f"contact created, {contact.json()}" 


