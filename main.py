import datetime
from worker import WorkThread
from fastapi import FastAPI,Request
import queue
from models import Task

queue_new_task = queue.Queue()
list_complite_task = []


app = FastAPI()

work_thread = WorkThread(queue_new_task,list_complite_task)

@app.on_event("startup")
async def startup():
    work_thread.start()

@app.on_event("shutdown")
async def shutdown():
    work_thread.stop()
@app.post('/task/create')
async def create_task(request: Request):
    req = await request.json()
    task:Task = Task(num=req['num'],time_sleep=req['time_sleep'],time_create=datetime.datetime.now())
    queue_new_task.put(task)
    print(task)
    return task.time_create
@app.get('/task/get_result')
async def get_task():
    return list_complite_task
@app.get('/task/get_queue')
async def get_queue_task():
    res_list = []
    for i in range(len(queue_new_task.queue)):
        res_list.append([i,queue_new_task.queue[i]])
    return res_list