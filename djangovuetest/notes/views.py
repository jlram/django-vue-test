from django.contrib.auth.models import User
from rest_framework import viewsets

from djangovuetest.notes.models import Note
from djangovuetest.notes.serializers import UserSerializer, NoteSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
