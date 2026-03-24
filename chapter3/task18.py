'''
Задача 5. Удаление заметки с Pydantic моделью в FastAPI
Задание:
Разработайте веб-приложение на фреймворке FastAPI, которое реализует эндпоинт для удаления заметки. У вас есть глобальный список notes для хранения заметок. Эндпоинт должен удалять заметку из списка notes по ID и возвращать удалённую модель.

Вам необходимо:

Определить Pydantic модель Note с полями id: int, text: str.
 
Реализовать эндпоинт, который принимает DELETE запрос по пути /notes/{note_id}. Он будет принимать note_id как параметр пути, удалять соответствующую заметку из списка notes и возвращать удалённую модель Note. Если заметка не найдена, выбросить HTTP-ошибку 404 с сообщением "Note not found".
То есть ответ эндпоинта должен быть следующий: JSON с данными удалённой заметки в формате модели Note (например, {"id": 1, "text": "Удалённая заметка"}).

Убедитесь, что вы импортировали все необходимые библиотеки, чтобы избежать ошибок при запуске приложения.
'''

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Annotated
app = FastAPI()

# Напишите здесь вашу модель.]
class Note(BaseModel):
    id: Annotated[int, Field(ge=0)]
    text: Annotated[str, Field()]


notes = [
    Note(id=1, text="Купить хлеб"),
    Note(id=2, text="Написать отчет"),
    Note(id=3, text="Позвонить маме"),
    Note(id=4, text="Сходить в спортзал"),
    Note(id=5, text="Прочитать книгу")
]

# Напишите здесь ваше решение.
@app.delete("/notes/{note_id}", response_model=Note, status_code=status.HTTP_200_OK)
async def delete_note(note_id: int) -> Note:
    for index, note in enumerate(notes):
        if note.id == note_id:
            notes.pop(index)
            return note
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Note not found")