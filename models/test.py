
# from models.Contact import Contact

from Contact import Contact


itay = Contact(ID="111111111", name="Itay shapira",phone="+972544391936", email="itay@efsdfs.com")
print("print1: ", itay.schema)
print("print2: ",itay.dict())
print("print3: ",itay.json())
print("print4: ",itay.schema())