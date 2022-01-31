from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import UserSerializer, UserRegisterSerializer
# Create your views here.

class RegisterAPIView(generics.GenericAPIView):
    # permission_classes = (HasAPIKey,)
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        logger.warning('register %s', request.user)
        logger.warning('register %s', request.user.is_authenticated)
        if request.user.is_authenticated:
            return Response({'status': 'You have already logged in!'}, status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
        },status=status.HTTP_201_CREATED)
