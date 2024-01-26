from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *

# Create your views here.

@api_view(["GET"])
def getRoutes(request):
    routes = [
        "GET /api --- coming soon"
    ]
    return Response(routes)

@api_view(["GET"])
def getNotes(request):
    notes = Notes.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def getNote(request, pk):
    note = Notes.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)