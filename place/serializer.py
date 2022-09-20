from rest_framework import serializers

from place.models import Place

class UserSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=64, required=False)
    last_name = serializers.CharField(max_length=64, required=False)
    email = serializers.CharField(max_length=128, required=False)

class PlaceSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    country = serializers.CharField(max_length=30, required=False)
    rating = serializers.IntegerField(min_value=0)
    description = serializers.CharField(max_length=512)
    image = serializers.CharField(required=False)
    created_by = UserSerializer(source='user_id', allow_null=True, required=False)

    def create(self, validated_data, *args, **kwargs):
        return Place.objects.create(**validated_data)

    def update(self, previous_instance, validated_data):
        previous_instance.update(**validated_data)
        previous_instance.save()

        return previous_instance
