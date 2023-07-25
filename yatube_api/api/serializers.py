from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

import datetime as dt

from posts.models import Group, Post, Comment, User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          queryset=User.objects.all(),
                                          )

    class Meta:
        model = Post
        fields = '__all__'
