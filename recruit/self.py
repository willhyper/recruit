from ._result import Result
from ._worker_interface import WorkerInterface


class Self(WorkerInterface):

    def __init__(self, func):
        self._func = func

    def send(self, *args, **kwargs) -> Result:
        r = self._func(*args, **kwargs)

        # conform with interface
        result = Result()
        result.set_result(r)
        return result
