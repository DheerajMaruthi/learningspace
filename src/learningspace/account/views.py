from django.shortcuts import render
from django.contrib.auth.models import Group

from rest_framework import generics, permissions
from .serializers import UserSerializer, UserRegisterSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status as response_status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from rest_framework import status
from rest_framework.exceptions import APIException
# Create your views here.

class RegisterAPIView(generics.GenericAPIView):
    # permission_classes = (HasAPIKey,)
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return Response({'status': 'You have already logged in!'}, status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.groups.add(Group.objects.get(name='Student'))
        user.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
        },status=status.HTTP_201_CREATED)
