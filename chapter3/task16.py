'''
Задача 3. Получение пользователя по ID с Pydantic моделью в FastAPI
Задание:
Разработайте веб-приложение на фреймворке FastAPI, которое реализует эндпоинт для получения пользователя по ID с использованием Pydantic модели для ответа. У вас есть глобальный in-memory список users для хранения объектов. Эндпоинт должен искать пользователя в списке users и возвращать модель пользователя или ошибку, если ID не найден.

Вам необходимо:

Определить Pydantic модель User с полями id: int, name: str, email: str.
 
Реализовать эндпоинт, который принимает GET запрос по пути /users/{user_id}. Он будет принимать user_id как параметр пути, искать объект в списке users и возвращать модель User, если найден.
То есть ответ эндпоинта должен быть следующий: JSON с данными пользователя в формате модели User, если ID существует, иначе HTTP-ошибка 404 с сообщением "User not found".

Убедитесь, что вы импортировали все необходимые библиотеки, чтобы избежать ошибок при запуске приложения.

'''


from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Annotated


app = FastAPI()

# Напишите здесь вашу модель.

class User(BaseModel):
    id: Annotated[int, Field(ge=0, description="id")]
    name: Annotated[str, Field(description="Имя")]
    email: Annotated[str, Field(description="Почта")]


users = [
    User(id=1, name="Алексей", email="alexey@example.com"),
    User(id=2, name="Мария", email="maria@example.com"),
    User(id=3, name="Иван", email="ivan@example.com"),
    User(id=4, name="Елена", email="elena@example.com"),
    User(id=5, name="Дмитрий", email="dmitry@example.com")
]



# Напишите здесь ваше решение.

@app.get("/users/{user_id}", response_model=User, status_code=status.HTTP_200_OK)
async def read_user(user_id: int) -> User:
    for user in users:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")