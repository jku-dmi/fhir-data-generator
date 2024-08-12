class FileRead(Exception):
    def __init__(self, message, errors):
        super(FileRead, self).__init__(message)
        self.message = message
        self.errors = errors
