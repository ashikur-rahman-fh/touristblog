from rest_framework import status

SUCCESS = {
    'status': status.HTTP_201_CREATED,
    'data': {'message': 'A new user created'},
}

PASSWORD_DID_NOT_MATCH = {
    'status': status.HTTP_400_BAD_REQUEST,
    'data': {'message': 'Password did not match'},
}

def EMPTY_FIELD(field):
    return {
        'status': status.HTTP_400_BAD_REQUEST,
        'data': {'message': f'Can not create user with emtpy {field}'},
    }
