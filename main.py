from assimilator.core.services import CRUDService
from click import password_option
from fastapi import FastAPI, Depends
from schema import UserSchema
from dependencies import get_crud

"""import smtplib
import os
from email.mime.text import MIMEText
from email.header import Header"""
from typing import List
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from assimilator.core.services import CRUDService
from dependencies import get_crud
import smtplib
from email.mime.text import MIMEText
app = FastAPI()

@app.get('/users')
async def list_users(crud: CRUDService = Depends(get_crud)):
    return crud.list()


@app.get('/users/{id}')
async def get_users(id: int, crud: CRUDService = Depends(get_crud)):
    return crud.get(id=id)


@app.post('/users')
async def create_user(user: UserSchema, crud: CRUDService = Depends(get_crud)):
    return crud.create(user.dict())


@app.delete('/users/{id}')
async def delete_user(id: int,crud: CRUDService = Depends(get_crud)):
    return crud.delete(id=id)


@app.put('/users/{id}')
async def update_user(id: int,user_data: UserSchema,crud: CRUDService = Depends(get_crud)):
    return crud.update(id=id ,update_data=user_data.dict())


@app.post('/users/{id}')
def send_ya_mail(recipients_emails: list, msg_text: str):
    login = 'adadadvlad659@gmail.com'
    #password = os.getenv('PASSWORD')
    password = Qwerty12344321
    msg = MIMEText(f'{msg_text}', 'plain', 'utf-8')
    msg['Subject'] = Header('test', 'utf-8')
    msh["From"] = login
    msh['To'] = ',' .join(mail)

    s = smtplib.SMTP('smtp.mail.google.com', 587, timeout=5)

    try:
        s.starttls()
        s.login(login, password)
        s.sendmail(msg['From'], email,msg.as_string())
    except Exception as ex:
        print(ex)
    finally:
        s.quit()



def main():
    send_ya_mail(mail=['twinker449@gmail.com'],msg_text='test')

if __name__ == '__main__':
    main()





