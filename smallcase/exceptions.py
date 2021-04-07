class BadRequestException(Exception):
    def __init__(self,message="Bad Request"):
        self.errorCode = 400
        self.errorMessage = message
        return