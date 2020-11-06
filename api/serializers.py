from rest_framework import serializers
from . import models


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ['id','title', 'content', 'author','date_posted']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = ['id','first_name', 'last_name', 'location', 'profile_info', 'picture']