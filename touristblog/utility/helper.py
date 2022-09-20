def get_drf_request_data(request, *args, **kwargs):
    return [request.data.get(key) for key in args]

def get_drf_request_payload(request, *args, **kawags):
    return {key : request.data.get(key) for key in args}

class ApiHelper:
    def __init__(self) -> None:
        pass

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
