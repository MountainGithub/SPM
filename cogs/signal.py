class Signal:
    def __init__(self):
        self.handlers = []

    def connect(self, handler):
        self.handlers.append(handler)

    def emit(self, *args, **kwargs):
        for handler in self.handlers:
            handler(*args, **kwargs)