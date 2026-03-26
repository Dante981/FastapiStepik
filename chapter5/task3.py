'''
Задача 3. Зависимость для проверки авторизации
Задание:
Разработайте веб-приложение на фреймворке FastAPI, которое реализует защищённый эндпоинт /profile с использованием механизма зависимостей. 
Эндпоинт должен проверять токен и возвращать сообщение "User is authorized" при успешной авторизации, иначе выбрасывать HTTPException с кодом 401.

Вам необходимо:

Определить зависимость check_auth, принимающую параметр token типа str через параметр запроса и возвращающую True, 
если полученный token равен "secret", иначе выбрасывающую HTTPException с кодом 401 и сообщением "Unauthorized".
 
Реализовать эндпоинт, который принимает GET запрос по пути /profile. 
Он будет использовать зависимость check_auth и возвращать строку "User is authorized" при успешной проверке.
То есть ответ эндпоинта должен быть следующий: строка "User is authorized", если токен валиден, иначе HTTP-ошибка 401 с сообщением "Unauthorized".

'''






from fastapi import FastAPI, Depends, HTTPException

async def check_auth(token: str) -> bool:
    if token == "secret":
        return True
    raise HTTPException(status_code=401, detail="Unauthorized")

app = FastAPI()

# Напишите здесь ваше решение.

@app.get("/profile")
async def get_profile(auth: list = Depends(check_auth)) -> str:
    if auth:
        return "User is authorized"
    raise HTTPException(status_code=401)
 