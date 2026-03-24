'''

Задача 4. Обновление пользователя с Pydantic моделью в FastAPI
Задание:
Разработайте веб-приложение на фреймворке FastAPI, которое реализует эндпоинт для обновления пользователя с использованием Pydantic модели для валидации обновлённых данных. У вас есть глобальный in-memory список users для хранения объектов. Эндпоинт должен принимать новые данные, обновлять объект в списке users и возвращать обновлённую модель.

Вам необходимо:

Определить Pydantic модель UserUpdate с полями name: str, age: int (с валидацией age > 0) для валидации входных данных.
 
Определить Pydantic модель User с полями id: int (автоматически присваивается), name: str, age: int для возврата созданного пользователя.
 
Реализовать эндпоинт, который принимает PUT запрос по пути /users/{user_id}. Он будет принимать user_id как параметр пути, тело запроса в формате модели UserUpdate, обновлять соответствующий объект в списке users и возвращать обновлённую модель User с id если он существует, иначе HTTP-ошибка 404 с сообщением "User not found".

Убедитесь, что вы импортировали все необходимые библиотеки, чтобы избежать ошибок при запуске приложения.

'''

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()

# Напишите здесь ваши модели.
class UserCreate(BaseModel):
    name: Annotated[str, Field(description="Имя")]
    age: Annotated[int, Field(gt=0)]

class UserUpdate(UserCreate):
    pass

class User(UserCreate):
    id: Annotated[int, Field(ge=0)]


users = [
    User(id=1, name="Алексей", age=25),
    User(id=2, name="Мария", age=30),
    User(id=3, name="Иван", age=22),
    User(id=4, name="Елена", age=28),
    User(id=5, name="Дмитрий", age=35)
]

# Напишите здесь ваше решение.
@app.put("/users/{user_id}", response_model= User, status_code=status.HTTP_200_OK)
async def update_user(user_id: int, user_update: UserUpdate) -> User:
    for index, user in enumerate(users):
        if user.id == user_id:
            new_user = User(id=user_id, name=user_update.name, age=user_update.age)
            users[index] = new_user
            return new_user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")