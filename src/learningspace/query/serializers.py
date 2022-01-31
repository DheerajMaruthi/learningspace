from datetime import datetime
import json

from django.db.models import Q

from account.models import User
from rest_framework import serializers
from .models import Query

class CreateQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = ('query','document')

class ListQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = ('query','response')


class AnswerQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Query
        fields = ('student','query','response')
        read_only_fields =  ('query','student')
