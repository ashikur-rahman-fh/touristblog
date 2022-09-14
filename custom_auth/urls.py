from django.urls import path, include
from rest_framework import routers

from dj_rest_auth.urls import urlpatterns as dj_rest_auth_urlpatterns
from dj_rest_auth.serializers import UserDetailsSerializer

from .views import RegistrationViewSet

router = routers.DefaultRouter()
router.register(r'registration', RegistrationViewSet, basename='registration')

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns.extend(dj_rest_auth_urlpatterns)
