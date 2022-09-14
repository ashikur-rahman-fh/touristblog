from os import stat
from rest_framework import status

SUCCESS = {
    'status': status.HTTP_201_CREATED,
    'message': 'A new user created',
}

PASSWORD_DID_NOT_MATCH = {
    'status': status.HTTP_400_BAD_REQUEST,
    'message': 'Password did not match',
}

def EMPTY_FIELD(field):
    return {
        'status': status.HTTP_400_BAD_REQUEST,
        'message': f'Can not create user with emtpy {field}',
    }
