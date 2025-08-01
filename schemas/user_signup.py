from pydantic import BaseModel

#same as user in database_models,becouser should full fill all the data need for user

class SignupRequest(BaseModel):
    email: str
    password: str
    name: str
    

class SignupResponse(BaseModel):
    email: str
    name: str
