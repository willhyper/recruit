import threading
from queue import Queue

from ._result import Result
from ._worker_interface import WorkerInterface


class FullTimeEmployee(WorkerInterface):

    def __init__(self, func):
        self._func = func
        self._q = Queue()
        self._t = threading.Thread(target=self._work)
        self._t.daemon = True
        self._t.start()

    def send(self, *args, **kwargs) -> Result:
        result = Result()  # wait to be set
        self._q.put_nowait((result, args, kwargs))
        return result

    def _work(self):
        while True:
            result, args, kwargs = self._q.get()  # work whenever there is new. otherwise idle

            r = self._func(*args, **kwargs)  # time-consuming task
            result.set_result(r)
