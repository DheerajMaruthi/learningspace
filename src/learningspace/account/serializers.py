from django.contrib.auth import authenticate
from . import models
from .models import User
from rest_framework import serializers





User._meta.get_field('email')._unique = True


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username', 'groups', 'email', 'phone')

    def get_plan(self, user):
        qs = UserSubscription.objects.filter(status=True, user=user)
        serializer = UserProfileSubscriptionSerializer(instance=qs, many=True)
        return serializer.data

class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'groups', 'email', 'password','phone']
        extra_kwargs = {'password': {'write_only': True}, 'groups': {'required': True}}


    def create(self, validated_data):
        # password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        return user
