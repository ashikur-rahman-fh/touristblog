from rest_framework import status

def NO_PLACE_FOUND(status_code):
    return {
        'data': {
            'message': 'Can not find place',
        },
        'status': status_code,
    }
