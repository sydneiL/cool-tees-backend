from rest_framework.generics import ListCreateAPIView
from .models import Favorite
from rest_framework import serializers


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'
        depth = 1 # to convert into array form the data


class FavoriteAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'