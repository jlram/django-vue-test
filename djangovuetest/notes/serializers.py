# Serializers del proyecto

# Serializer del usuario
from django.contrib.auth.models import User
from rest_framework import serializers

from djangovuetest.notes.models import Note


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'id']


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

