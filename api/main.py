from fastapi import FastAPI
from db import session
from model import TaskTable, Task

app = FastAPI()


# タスクデータの取得
@app.get("/task")
def read_task_list():
    tasks = session.query(TaskTable).all()
    return tasks


# id指定によるタスクデータの取得
@app.get("/task/{task_id}")
def read_task(task_id: int):
    task = session.query(TaskTable).filter(TaskTable.id == task_id).first()
    return task


# タスクデータの追加
@app.post("/task")
def add_task(task: Task):
    session.add(task)
    session.commit()


# タスクデータの更新
@app.put("/task/{task_id}")
def update_task(task: Task, user_id: int):
    update_task = session.query(TaskTable).filter(TaskTable.id == user_id).first()
    update_task.title = task.title
    update_task.done = task.done
    session.commit()
