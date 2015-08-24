class APIResponseFailure(Exception):
    def __init__(self, body=None):
        message = ('Failed to retrieve an item price successfully!'
                   ' <body={}>').format(body)

        super(APIResponseFailure, self).__init__(message)
