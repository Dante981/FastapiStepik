from fastapi import FastAPI, Depends, Query, HTTPException
from pydantic import BaseModel
from starlette import status

async def pagination_path_func(page: int):
    if page < 0:
        raise HTTPException(status_code=404, detail="Page does not exist")
    if page == 0:
        raise HTTPException(status_code=400, detail="Invalid page value")

async def pagination_func(limit: int = Query(10, gt=0), page: int = 1):
    return {'limit': limit, 'page': page}

app = FastAPI()



@app.get("/messages", dependencies=[Depends(pagination_path_func)])
async def all_messages(pagination: dict = Depends(pagination_func)):
    return {"messages": pagination}

