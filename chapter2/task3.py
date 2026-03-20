'''
Напишите код приложения на FastAPI, в котором асинхронная функция retrieve_user_profile() будет принимать GET-запрос по маршруту /users, получая обязательный строковый параметр запроса username.

Для параметра username используется валидатор Query со следующими параметрами:

Значение должно быть от 2 до 50 символов включительно
Описание поля 'Имя пользователя'
Эндпоинт должен возвращать значение для ключа, полученного из значения параметра username, словаря profiles_dict.

А если такой ключ отсутствует в словаре profiles_dict, необходимо вернуть словарь с ключом 'message' и значением 'Пользователь <значение параметра запроса> не найден.'.


P.S. На экран ничего не нужно выводить, пример словаря profiles_dict, глобальная переменная, пример словаря добавлять в решение не нужно.

profiles_dict = {
    'alex': {'name': 'Александр', 'age': 33, 'phone': '+79463456789', 'email': 'alex@my-site.com'},
    ...
}

                  

Пример запроса:

/users?username=alex

                  
ответ для него:

{'name': 'Александр', 'age': 33, 'phone': '+79463456789', 'email': 'alex@my-site.com'}

                  

Пример запроса для не существующего пользователя:

/users?username=roman

                  
ответ для него:

{'message': 'Пользователь roman не найден.'}

'''


from typing import Annotated
from fastapi import FastAPI, Query, Path
app = FastAPI()

@app.get("/users")
async def retrieve_user_profile(username: Annotated[str, Query(min_length=2, max_length=50, description="Имя пользователя")]) -> dict:
    return profiles_dict[username] if username in profiles_dict.keys() else {'message': f'Пользователь {username} не найден.'}