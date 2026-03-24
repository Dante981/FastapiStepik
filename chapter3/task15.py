'''
Задача 2. Создание пользователя с Pydantic моделями в FastAPI
Задание:
Разработайте веб-приложение на фреймворке FastAPI, которое реализует эндпоинт для создания нового пользователя с использованием Pydantic моделей для валидации входных данных и формирования ответа. У вас есть глобальный in-memory список users для хранения объектов. Эндпоинт должен принимать данные пользователя, добавлять его в список users и возвращать созданную модель в ответе.

Вам необходимо:

Определить Pydantic модель UserCreate с полями name: str, age: int (с валидацией age >= 18) для валидации входных данных.
 
Определить Pydantic модель User с полями id: int (автоматически присваивается), name: str, age: int (с валидацией age >= 18) для возврата созданного пользователя.
 
Реализовать эндпоинт, который принимает POST запрос по пути /users. Он будет принимать тело запроса в формате модели UserCreate, добавлять объект в список users с присвоением id (например, длина списка + 1) и возвращать ответ в виде модели User.
То есть ответ эндпоинта должен быть следующий: JSON с данными созданного пользователя в формате модели User.

Убедитесь, что вы импортировали все необходимые библиотеки, чтобы избежать ошибок при запуске приложения.

'''

from fastapi import FastAPI, status
from pydantic import BaseModel, Field

class User(BaseModel):
    id: int = Field(ge=0 ,description="id пользователя")
    name: str = Field(description="Имя")
    age: int = Field(ge=18, description="Возраст")


class UserCreate(BaseModel):
    name: str = Field(description="Имя")
    age: int = Field(ge=18, description="Возраст")


app = FastAPI()

users = []

@app.post("/users", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user_create: UserCreate) -> User:
    next_id = max((us.id for us in users), default=-1) + 1
    new_user = User(id=next_id, name=user_create.name, age=user_create.age)
    users.append(new_user)
    return new_user
