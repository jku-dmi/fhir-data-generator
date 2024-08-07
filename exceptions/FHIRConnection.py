class FHIRConnectionException(Exception):
    def __init__(self, message, errors):
        super(FHIRConnectionException, self).__init__(message)
        self.message = message
        self.errors = errors
