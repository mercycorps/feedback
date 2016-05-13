import json
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers.python import Serializer as PythonSerializer

from django.utils import six
from django.contrib.auth.models import User, Group

from rest_framework import serializers
from rest_framework.response import Response

from djangocosign.models import Region, Country, Office
from .models import Comment, Feedback


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ("issue_type", "summary", "description", "reference", "tags", "status", "resolution", "annotation", "votes_up", "votes_dn")
