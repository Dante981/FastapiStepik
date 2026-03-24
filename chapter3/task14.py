'''
Задача 1. Получение списка задач с Pydantic моделью в FastAPI
Задание:
Разработайте веб-приложение на фреймворке FastAPI, которое реализует эндпоинт для получения списка задач с использованием Pydantic модели для ответа. У вас есть глобальный in-memory список tasks для хранения объектов. Эндпоинт должен возвращать весь список tasks в формате моделей.

Вам необходимо:

Определить Pydantic модель Task с полями id: int, title: str, completed: bool.
 
Реализовать эндпоинт, который принимает GET запрос по пути /tasks. Он должен возвращать весь список tasks в формате list[Task]. То есть ответ эндпоинта должен быть следующий: JSON со списком задач в формате list[Task].

Убедитесь, что вы импортировали все необходимые библиотеки, чтобы избежать ошибок при запуске приложения.

'''


from fastapi import FastAPI, status
from pydantic import BaseModel, Field




class Task(BaseModel):
    id: int = Field(description="id задачи")
    title: str = Field(description="Название задачи")
    completed: bool = Field(default=False, description="Выполнена")



app = FastAPI()


tasks = [
    Task(id=1, title="Купить молоко", completed=False),
    Task(id=2, title="Позвонить другу", completed=True),
    Task(id=3, title="Сделать домашку", completed=False),
    Task(id=4, title="Погулять с собакой", completed=True),
    Task(id=5, title="Записаться на тренировку", completed=False)
]


@app.get("/tasks", response_model=list[Task], status_code=status.HTTP_200_OK)
async def read_tasks() -> list[Task]:
    return tasks


