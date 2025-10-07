from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

tasks = []

class Task(BaseModel):
    title: str

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API de tarefas com FastAPI!"}

@app.get("/tasks", response_model=List[Task])
def get_tasks():
    return tasks

@app.post("/tasks", response_model=Task)
def add_task(task: Task):
    tasks.append(task)
    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    if 0 <= task_id < len(tasks):
        removed = tasks.pop(task_id)
        return {"message": f"Tarefa removida: {removed.title}"}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")
