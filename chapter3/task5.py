'''
Задача 5: Удаление цели
Задание:
Создайте приложение с эндпоинтом для удаления цели. Цели хранятся в словаре goals_db (id: goal).

Эндпоинт:

DELETE /goals/{goal_id} — если goal_id есть, то удаляет и возвращает "Goal deleted!", а если goal_id нет, то возвращается "Goal not found" с кодом ответа 404.

Пример: DELETE /goals/0 → "Goal deleted!".

'''



from fastapi import FastAPI, status, HTTPException

app = FastAPI()

goals_db = {0: "Learn FastAPI basics",
            1: "Build CRUD app",
            2: "Write tests with TestClient",
            3: "Add authentication",
            4: "Deploy to production"}

@app.delete("/goals/{goal_id}", status_code=status.HTTP_200_OK)
async def delete_gpal(goal_id: int) -> str:
    if goal_id not in goals_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Goal not found")
    else:
        goals_db.pop(goal_id)
        return "Goal deleted!"