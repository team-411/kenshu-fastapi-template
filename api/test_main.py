from fastapi.testclient import TestClient
from main import app
from db import session
from model import TaskTable

client = TestClient(app)

# 正常系
def test_get_tasks_NR001_タスクの一覽取得():
    session.query(TaskTable).delete()
    session.commit()
    session.add(TaskTable(id=1, title="test", done=1))
    session.commit()
    
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == [
        {          
            "id":1,
            "title":"test",
            "done":1
        }
    ]
    
def test_put_tasks_NR002_タスクの更新():
    id = 1
    session.query(TaskTable).delete()
    session.commit()
    session.add(TaskTable(id=id, title="olddata", done=0))
    session.commit()
    
    response = client.put(f"/tasks/{id}", json={"title":"newdata", "done":1})
    assert response.status_code == 200
    
    updated_data = session.query(TaskTable).filter(TaskTable.id == id).first()
    assert updated_data.id == id
    assert updated_data.title == "newdata"
    assert updated_data.done == 1
    
    
def test_post_tasks_NR003_タスクの追加():
    session.query(TaskTable).delete()
    session.commit()
    session.add(TaskTable(id=1, title="test", done=1))
    session.commit()
    
    response = client.post("/tasks", json={"title":"test2"})
    assert response.status_code == 200
    
    assert session.query(TaskTable).count() == 2
    
    new_data = session.query(TaskTable).order_by(TaskTable.id.desc()).first()
    assert new_data.title == "test2"
    assert new_data.done == 0

# 異常系
def test_put_tasks_ABR001_タスクの更新_存在しないタスクIDを指定():
    id = 1
    session.query(TaskTable).delete()
    session.commit()
    session.add(TaskTable(id=id, title="olddata", done=0))
    session.commit()
    
    response = client.put(f"/tasks/{id+1}", json={"title":"newdata", "done":1})
    assert response.status_code == 404
    
    updated_data = session.query(TaskTable).filter(TaskTable.id == id).first()
    assert updated_data.id == id
    assert updated_data.title == "olddata"
    assert updated_data.done == 0
    
def test_put_tasks_ABR002_タスクの更新_タイトルが空():
    id = 1
    session.query(TaskTable).delete()
    session.commit()
    session.add(TaskTable(id=id, title="olddata", done=0))
    session.commit()
    
    response = client.put(f"/tasks/{id}", json={"title":"", "done":1})
    assert response.status_code == 400
    
    updated_data = session.query(TaskTable).filter(TaskTable.id == id).first()
    assert updated_data.id == id
    assert updated_data.title == "olddata"
    assert updated_data.done == 0

def test_post_tasks_ABR003_タスクの追加_タイトルが空():
    session.query(TaskTable).delete()
    session.commit()
    session.add(TaskTable(id=1, title="test", done=1))
    session.commit()
    
    response = client.post("/tasks", json={"title":""})
    assert response.status_code == 400
    
    assert session.query(TaskTable).count() == 1
    
    new_data = session.query(TaskTable).order_by(TaskTable.id.desc()).first()
    assert new_data.title == "test"
    assert new_data.done == 1
