from fastapi.testclient import TestClient

import main


client = TestClient(main.app)


def setup_function():
    main.todos.clear()


def test_todo_crud_flow():
    todo = {
        "id": 1,
        "title": "Write tests",
        "description": "Add API coverage",
        "completed": False,
    }
    updated_todo = {
        **todo,
        "title": "Write API tests",
        "completed": True,
    }

    create_response = client.post("/todos", json=todo)
    assert create_response.status_code == 200
    assert create_response.json() == {
        "message": "Todo created successfully",
        "data": todo,
    }

    list_response = client.get("/todos")
    assert list_response.status_code == 200
    assert list_response.json() == {"data": [todo]}

    get_response = client.get("/todos/1")
    assert get_response.status_code == 200
    assert get_response.json() == {"data": todo}

    update_response = client.put("/todos/1", json=updated_todo)
    assert update_response.status_code == 200
    assert update_response.json() == {
        "message": "Todo updated successfully",
        "data": updated_todo,
    }

    delete_response = client.delete("/todos/1")
    assert delete_response.status_code == 200
    assert delete_response.json() == {"message": "Todo deleted successfully"}

    missing_response = client.get("/todos/1")
    assert missing_response.status_code == 200
    assert missing_response.json() == {"message": "Todo not found"}