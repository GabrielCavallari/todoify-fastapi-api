from fastapi import FastAPI, HTTPException
from typing import List
from models import Todo

app = FastAPI()

db_todos = [
    Todo(id=1, title="Aprender FastAPI", description="Estudar o guia", completed=True),
    Todo(id=2, title="Construir a API Todoify", description="Seguir o projeto prático"),
]
# Rota para Criar uma nova tarefa (Create)
@app.post("/todos", response_model=Todo)
def create_todo(todo: Todo):
    db_todos.append(todo)
    return todo

@app.get("/todos", response_model=List[Todo])
def get_todos():
    return db_todos

@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo_by_id(todo_id: int):
    for todo in db_todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(db_todos):
        if todo.id == todo_id:
            db_todos[index] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(db_todos):
        if todo.id == todo_id:
            db_todos.pop(index)
            return {"message": "Tarefa excluída com sucesso"}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")