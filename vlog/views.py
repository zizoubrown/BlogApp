from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from .models import Profile, Post

# Create your views here.

class Post(APIView):

    def get(self, request):
        post = Post.objects.all()
        serializer = serializers.PostSerializer(post, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDetail(APIView):

    def get(self, request, post_id):
        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            raise Http404
        serializer = serializers.PostSerializer(post)
        return Response(serializer.data)

    def delete(self, request, post_id):
        try:
            post = Post.objects.get(pk=post_id)
        except Post.DoesNotExist:
            raise Http404
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)