from pydantic import BaseModel
#from assimilator.core.database.models import BaseModel


class UserSchema(BaseModel):
    firstname: str
    lastname: str
    mail: str
