class PayoneException(Exception):
    pass

class PayoneServerException(PayoneException):
    def __init__(self, message, code=None):
        super(PayoneServerException, self).__init__(message)
        self.code = code
