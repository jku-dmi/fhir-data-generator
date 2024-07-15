class ResourceNotFound(Exception):
    def __init__(self, message, errors):
        super(ResourceNotFound, self).__init__(message)
        self.message = message
        self.errors = errors
