from rest_framework import serializers
from . import models


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Restaurant
        fields = ['title', 'content', 'author']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Restaurant
        fields = ['first_name', 'last_name', 'location', 'profile_info', 'picture']