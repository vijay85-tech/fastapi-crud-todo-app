from fastapi import FastAPI
from pydantic import BaseModel

app =  FastAPI()

todos = []

class Todo(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False

#Create a new todo
@app.post("/todos")
def create_todo(todo:Todo):
    todos.append(todo)
    return {"message": "Todo created successfully", "data": todo}

#Fetch all todos
@app.get("/todos")
def get_todos():
    if not todos:
        return {"message": "No todos found!"}
    return {"data": todos}

#get single todo baised on todo id
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"data": todo}
    return {"message": "Todo not found"}

#update todo based on todo id
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[i] = updated_todo
            return {"message": "Todo updated successfully", "data": updated_todo}
    return {"message": "Todo not found"}

#delete todo based on todo id
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(i)
            return {"message": "Todo deleted successfully"}
    return {"message": "Todo not found"}


