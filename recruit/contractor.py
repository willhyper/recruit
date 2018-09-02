import threading
from functools import partial

from ._worker_interface import WorkerInterface
from ._result import Result


class Contractor(WorkerInterface):

    def __init__(self, func):
        self._func = func

        self._result = None

        def _func(*args, **kwargs):
            self._result = Result()
            r = self._func(*args, **kwargs)  # time-consuming task
            self._result.set_result(r)

        self._t = partial(threading.Thread, target=_func)

    def send(self, *args, **kwargs) -> Result:
        self._t(args=args, kwargs=kwargs).start() # spawn a new contractor

        return self._result
