import threading
from time import sleep
from models import Task

class WorkThread(threading.Thread):
    def __init__(self,q,list_res):
        threading.Thread.__init__(self)
        self._q = q
        self._list_res = list_res
        self._bool_work = True
    def run(self):
        while(self._bool_work):
            if(self._q.empty()):
                sleep(0.3)
                continue
            item = self._q.get().dict()
            num = item['num']
            time_sleep = item['time_sleep']
            sleep(time_sleep)
            self._list_res.append(num)
    def stop(self):
        self._bool_work=False