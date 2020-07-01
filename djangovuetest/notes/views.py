import datetime

from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import viewsets, status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from djangovuetest.notes.models import Note
from djangovuetest.notes.serializers import UserSerializer, NoteSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class NoteView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        queryset = Note.objects.all().order_by('-id')
        serializer = NoteSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = NoteSerializer(data=request.data)

        serializer.initial_data['task'] = True if serializer.initial_data['task'] == 'true' else False
        serializer.initial_data['user'] = User.objects.filter(username=serializer.initial_data['user']).first().id


        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

