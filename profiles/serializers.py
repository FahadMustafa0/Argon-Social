from rest_framework import serializers
from .models import profile
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class ProfileSerializer(serializers.ModelSerializer):
    following = UserSerializer(many=True, read_only=True)
    followers =  UserSerializer(many=True, read_only=True)
    # user =UserSerializer( read_only=True)
    class Meta:
        model = profile
        fields = ['first_name',
                'last_name',
                #   'user',
                  'following',
                  'followers',
                  'bio',
                  'email',
                  'country',
                  'avatar',
                  'updated',
                  'created',
                  ]

class ProfileUpdateSerializer(serializers.ModelSerializer):
    following = UserSerializer(many=True, read_only=True)
    followers =  UserSerializer(many=True, read_only=True)

    class Meta:
        model = profile
        fields = ['first_name',
                  'last_name',
                  'user',
                  'following',
                  'followers',
                  'bio',
                  'email',
                  'country',
                  'avatar',
                  ]
    