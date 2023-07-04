from fastapi import FastAPI
from db import session
from model import TaskTable
from schema import Task, TaskCreate, TaskUpdate

app = FastAPI()


# タスクデータの取得
@app.get("/tasks")
def read_task_list():
    tasks = session.query(TaskTable).all()
    return tasks


# id指定によるタスクデータの取得
@app.get("/tasks/{task_id}")
def read_task(task_id: int):
    task = session.query(TaskTable).filter(TaskTable.id == task_id).first()
    return task


# タスクデータの追加
@app.post("/tasks")
def create_task(task: TaskCreate):
    add_task = TaskTable(
        title=task.title,
        done=0
    )
    
    session.add(add_task)
    session.commit()


# タスクデータの更新
@app.put("/tasks/{task_id}")
def update_task(task: TaskUpdate, task_id: int):
    update_task = session.query(TaskTable).filter(TaskTable.id == task_id).first()
    update_task.title = task.title
    update_task.done = task.done
    session.commit()
