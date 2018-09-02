import threading


class Result:

    def __init__(self):
        self._event = threading.Event()

    def set_result(self, result):
        self._result = result
        self._event.set()

    def get_result(self):
        self._event.wait()
        return self._result

    def __repr__(self) -> str:
        return str(self.get_result())
