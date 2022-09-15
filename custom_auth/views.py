from django.shortcuts import render

from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from touristblog.utility.helper import get_drf_request_data

from .constants.response import registration

# Create your views here.

class RegistrationViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def create(self, request):
        post_data = request.data
        firstname, lastname, username, email, password_1, password_2 = get_drf_request_data(
            request, 'firstname', 'lastname', 'username', 'email', 'password_1', 'password_2',
        )

        if password_1 != password_2:
            return Response(**registration.PASSWORD_DID_NOT_MATCH)

        if not username:
            return Response(**registration.EMPTY_FIELD('username'))

        if not password_1:
            return Response(**registration.EMPTY_FIELD('password'))

        user = User.objects.create_user(username=username, email=email, password=password_1, first_name=firstname, last_name=lastname)
        user.save()

        return Response(**registration.SUCCESS)
