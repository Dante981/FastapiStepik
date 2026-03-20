''''
Напишите код приложения на FastAPI, в котором асинхронная функция get_user() будет принимать GET-запрос по маршруту /users/<name>, получая строковый параметр пути name и использует валидатор Path со следующими параметрами:

Минимальная длина строки 4 символа
Максимальная длина строки 20 символов
Описание поля Enter your name
Эндпоинт должен возвращать словарь с ключом user_name и значением параметра name.


P.S. На экран ничего не нужно выводить, пример запроса:

/users/Alex

                  
ответ для него:

{'user_name': 'Alex'}

'''

from typing import Annotated
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/users/{name}")
async def get_user(name: str = Path(min_length=4, max_length=20, description = "Enter your name")) -> dict:
    return {'user_name': name}