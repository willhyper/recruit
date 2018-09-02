from ._result import Result


class WorkerInterface:

    def send(self, *args, **kwargs)->Result:
        pass