import json
import logging
import time
from datetime import datetime

from django.conf import settings

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.db.models import F

from django.utils.decorators import method_decorator
from django.http import Http404

from rest_framework.exceptions import NotFound
from rest_framework.pagination import PageNumberPagination

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status as response_status
from rest_framework.decorators import permission_classes, api_view
from rest_framework.authentication import BaseAuthentication, get_authorization_header
from rest_framework import status
from rest_framework.exceptions import APIException

from .models import Query
from .permissions import IsStudent,IsMentor
from .serializers import CreateQuerySerializer,ListQuerySerializer,AnswerQuerySerializer

from learningspace.threadings import send_mail

class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100000

    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'paginationCurrent': self.page.number,
            'paginationTotal': self.page.paginator.count,
            'results': data
        })

class CreateQueryView(generics.CreateAPIView):
    permission_classes = (IsStudent)
    model = Query
    serializer_class = CreateQuerySerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        headers = self.get_success_headers(serializer.data)
        data = {'query': instance.query}
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


class QueryView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ListQuerySerializer
    queryset = Query.objects.all()
    pagination_class = CustomPagination
    filterset_fields = {
       'created_on': ['query', 'student']
   }

    def get_queryset(self):
        if self.request.user.is_student:
            cat = Query.objects.filter(student=self.request.user)
        else:
            cat = Query.objects.filter(answered=False)
        if cat:
            return cat
        else:
            raise NotFound()

class AnswerQueryView(generics.UpdateAPIView):
    permission_classes = (IsMentor,)
    model = Query
    serializer_class = AnswerQuerySerializer

    def post(self, request, *args, **kwargs):
        serializer = AnswerQuerySerializer(data=request.data, instance=obj, partial=True)
        serializer.is_valid(raise_exception=True)
        query = serializer.save(answered=True,mentor=self.request.user)
        subject = 'New notification! Response from mentor'
        from_email = "test@gmail.com"
        data = query.id
        template_object = render_to_string(
            'notification.html',data)
        send_mail(subject=subject, template_object=template_object,
        from_email=from_email, to=[query.student.email], resume=None,
        fail_silently=False)
        return Response("Answered Successfully")
