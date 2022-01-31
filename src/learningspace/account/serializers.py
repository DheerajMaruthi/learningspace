from django.contrib.auth import authenticate
from . import models
from .models import User
from rest_framework import serializers





User._meta.get_field('email')._unique = True


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'groups', 'email', 'phone')

    def get_plan(self, user):
        qs = UserSubscription.objects.filter(status=True, user=user)
        serializer = UserProfileSubscriptionSerializer(instance=qs, many=True)
        return serializer.data

class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password','phone']
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        # password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        return user
