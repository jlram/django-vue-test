import datetime

from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import viewsets, status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from djangovuetest.notes.models import Note
from djangovuetest.notes.serializers import UserSerializer, NoteSerializer
from rest_framework.parsers import MultiPartParser, FormParser


# Viewset de usuarios con el cual recibimos una query de todos los usuarios de la aplicacion
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# APIView de las Notes, en la cual diferenciamos los metodos get y post para actuar
# segun convenga
class NoteView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        """
            Devuelve todas las Notes, de manera inversa segun su id
            para asi mostrar en la tabla primero la más reciente.
        :param request:
        :return serializer.data:
        """
        queryset = Note.objects.all().order_by('-id')
        serializer = NoteSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        """
            Crea una nueva Note, modificamos primero los campos task y user
            para que indiquen un valor booleano y la id del usuario, y despues
            comprobamos que todos los datos se han rellenado correctamente
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        serializer = NoteSerializer(data=request.data)

        serializer.initial_data['task'] = True if serializer.initial_data['task'] == 'true' else False
        serializer.initial_data['user'] = User.objects.filter(username=serializer.initial_data['user']).first().id

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

