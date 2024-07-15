class ResourceNotAvailable(Exception):
    def __init__(self, message, errors):
        super(ResourceNotAvailable, self).__init__(message)
        self.message = message
        self.errors = errors
