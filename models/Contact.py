from pydantic import BaseModel, validator, EmailStr
import phonenumbers
class Contact(BaseModel):
    ID: str
    name: str
    phone: str
    email: EmailStr

    @validator('ID')
    def validate_ID(cls,v):
        if len(v) < 9:
            raise ValueError('ID must contain nine digits')
        if not v.isdigit():
            raise ValueError('ID must contain only digits')
        return v

    @validator('name')
    def name_must_contain_space(cls, v):
        if ' ' not in v:
            raise ValueError('must contain a space')
        return v
    
    @validator('phone')
    def validate_phone(cls, v):
        phone = phonenumbers.parse(v, "IL")
        if not phonenumbers.is_valid_number(phone):
            raise ValueError('phone entered is not a valid number')
        return v
    
    def __repr__(self) -> str:
        return f'ID: {self.ID}, name: {self.name}, phone:{self.phone}, email:{self.email}|'