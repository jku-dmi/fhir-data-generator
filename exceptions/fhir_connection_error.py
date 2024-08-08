class FhirConnection(Exception):
    def __init__(self, message, errors):
        super(FhirConnection, self).__init__(message)
        self.message = message
        self.errors = errors
