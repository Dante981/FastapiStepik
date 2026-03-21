'''
Задача 2: Чтение одной задачи
Задание:
Создайте приложение с эндпоинтом для чтения одной задачи по id.  Задачи хранятся в словаре tasks_db (в формате id: title).

Эндпоинт:

GET /tasks/{task_id} — который возвращает текст задачи по task_id. 
Если задача существует — вернуть строку с её текстом.
Если задача не существует — вернуть строку "Task not found"  с 404 кодом ответа.
 
Пример: GET /tasks/0 → "Study FastAPI".

'''


from fastapi import FastAPI, status, HTTPException

app = FastAPI()

tasks_db = {0: "Study FastAPI", 1: "I like FastAPI"}

@app.get("/tasks/{tasks_id}", status_code=status.HTTP_200_OK)
async def read_task(tasks_id: int) -> str:
    try:
        return tasks_db[tasks_id]
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")