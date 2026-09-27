from fastapi import FastAPI, status,HTTPException
from pydantic import BaseModel

app =  FastAPI()

todos = []

class Todo(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False

#Create a new todo
@app.post("/todos", status_code=status.HTTP_201_CREATED)
def create_todo(todo:Todo):
    todos.append(todo)
    return {"message": "Todo created successfully", "data": todo, "status_code": status.HTTP_201_CREATED}

#Fetch all todos
@app.get("/todos", status_code=status.HTTP_200_OK)
def get_todos():
    if not todos:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No todos found!")
    return {"data": todos}

#get single todo baised on todo id
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"data": todo}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")

#update todo based on todo id
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[i] = updated_todo
            return {"message": "Todo updated successfully", "data": updated_todo}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found")

#delete todo based on todo id
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(i)
            return {"message": "Todo deleted successfully"}
    return {"message": "Todo not found"}




class User(BaseModel):
    name: str
    email: str
    password: str

class UserResponse(BaseModel):
    name: str
    email: str

@app.get("/users", response_model=UserResponse)
def get_user():
    return {"name": "John Doe", "email": "john.doe@example.com", "password": "secret", "address": "123 Main St"}  # The password will be hidden in the response

