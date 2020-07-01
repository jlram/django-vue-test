# Serializers del proyecto

# Serializer del usuario
from django.contrib.auth.models import User
from rest_framework import serializers

from djangovuetest.notes.models import Note


# Serializador para motrar una informacion determinada del usuario en la API
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'id']


# Serializador para motrar una informacion determinada de las Notes en la API
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'date', 'end_date', 'note', 'adjunto', 'user', 'task', 'tag', 'type']
