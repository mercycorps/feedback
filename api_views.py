from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from .serializers import *
from .models import Feedback, Comment



class IsModerator(permissions.BasePermission):
    """
    permission check for moderators to change status of an issue
    """
    def has_permission(self, request, view):
        return request.user.groups.filter(name="moderator").exists()


class FeedbackViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows feedback to be viewed or edited.
    """
    queryset = Feedback.objects.all().order_by('-created')
    serializer_class = FeedbackSerializer
    permission_classes = [IsModerator]
