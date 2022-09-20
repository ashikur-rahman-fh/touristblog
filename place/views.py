from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from place.models import Place
from place.serializer import PlaceSerializer

from place.constants.response import NO_PLACE_FOUND
# Create your views here.

class PlaceViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    def list(self, request):
        places = Place.objects.all()
        serialized_places = PlaceSerializer(places, many=True)

        return Response(serialized_places.data)

    def create(self, request):
        data = request.data
        place_serializer = PlaceSerializer(data=data)
        place_serializer.is_valid(raise_exception=True)

        place = place_serializer.save(user_id=request.user)

        return Response(data=place_serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk):
        try:
            place = Place.objects.get(id=pk)
        except:
            return Response(**NO_PLACE_FOUND(status.HTTP_404_NOT_FOUND))
        serialized_place = PlaceSerializer(place)

        return Response(serialized_place.data)

    def update(self, request, pk=None):
        try:
            previous_place = Place.objects.get(id=pk)
        except:
            return Response(**NO_PLACE_FOUND(status.HTTP_400_BAD_REQUEST))

        place_serializer = PlaceSerializer(previous_place, data=request.data)
        place_serializer.is_valid(raise_exception=True)

        new_place = place_serializer.save()

        return Response(data=place_serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        try:
            place = Place.objects.get(id=pk)
        except:
            return Response(**NO_PLACE_FOUND(status.HTTP_400_BAD_REQUEST))

        place.delete()

        return Response(status=status.HTTP_200_OK)
