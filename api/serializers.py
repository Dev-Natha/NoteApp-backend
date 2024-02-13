from rest_framework.serializers import ModelSerializer
from .models import Notes
from django.contrib.auth.models import User

class NoteSerializer(ModelSerializer):
    class Meta:
        model = Notes
        fields = "__all__"

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"