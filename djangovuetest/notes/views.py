import datetime

from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response

from djangovuetest.notes.models import Note
from djangovuetest.notes.serializers import UserSerializer, NoteSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def create(self, validated_data):
        note = Note.objects.create(
            end_date=validated_data.data['end_date'],
            note=validated_data.data['note'],
            user=User.objects.filter(username=validated_data.data['user']).first(),
            task=validated_data.data['task'],
            tag=validated_data.data['tag'],
            type=validated_data.data['type'],
        )

        return HttpResponse(status=200) if note else HttpResponse(status=400)

