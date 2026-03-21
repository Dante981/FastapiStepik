'''
Задача 4: Обновление цитаты
Задание:
Создайте приложение с эндпоинтом для обновления цитаты. Цитаты хранятся в словаре quotes_db (формат id: quote).

Эндпоинт:

PUT /quotes/{quote_id} — принимает новый текст цитаты через Body(...) (один строковый параметр) и обновляет текст цитаты по quote_id возвращая "Quote updated!". Если цитата не найдена, выводится текст "Quote not found" с кодом ответа 404.

Пример: PUT /quotes/0 "FastAPI is the best framework" → "Quote updated!". 

'''


from fastapi import FastAPI, Body, status, HTTPException

app = FastAPI()

quotes_db = {0: "FastAPI lets you build APIs fast with type hints",
              1: "Auto docs at /docs and /redoc with OpenAPI",
              2: "Pydantic validates your data",
              3: "Depends gives clean Dependency Injection",
              4: "Use async def and await for concurrency"}


@app.put("/quotes/{quote_id}", status_code=status.HTTP_200_OK) 
async def update_quote(quote_id: int, text: str = Body(...)) -> str:
    if quote_id not in quotes_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Quote not found")
    else:
        quotes_db[quote_id] = text
        return "Quote updated!"
