from rest_framework import serializers
from django.contrib.auth import get_user_model, password_validation
from django.contrib.auth.models import BaseUserManager
from rest_framework.authtoken.models import Token
from .models import Post


User = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'author', 'title', 'body', 'created_at',)
        model = Post

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=300, required=True)
    password = serializers.CharField(required=True, write_only=True)

class AuthUserSerializer(serializers.ModelSerializer):
    # auth_token = serializers.SerializerMethodField()
    class Meta:
         model = User
         fields = ('id', 'email', 'username')
        #  read_only_fields = ('id', 'auth_token')
    
    def get_auth_token(self, obj):
        token = Token.objects.create(user=obj)
        return token.key

class EmptySerializer(serializers.Serializer):
    pass
