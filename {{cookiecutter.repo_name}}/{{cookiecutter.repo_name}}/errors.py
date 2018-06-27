import time


class APIError(Exception):
    def __init__(self, message=None, code=400):
        self.message = message
        self.code = code

    def to_dict(self):
        return {"code": self.code, "message": self.message, "timestamp": time.time()}


class BadRequest(APIError):
    def __init__(self, message):
        self.message = message
        self.code = 400
        super().__init__(self.message, self.code)
