from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *

# Create your views here.

@api_view(["GET"])
def getRoutes(request):
    routes = [
        "GET /note"
        "GET /note/:id"
    ]
    return Response(routes)

@api_view(["GET", "POST"])
def getNotes(request):
    if request.method == "POST":
        Notes.objects.create(title=request.data['title'], body=request.data['body'])
    notes = Notes.objects.all().order_by("-updated")
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)

@api_view(["GET", "PUT", "DELETE"])
def handleNote(request, pk):
    note = Notes.objects.get(id=pk)
    if request.method == "GET":
        serializer = NoteSerializer(note, many=False)
    elif request.method == "PUT":
        serializer = NoteSerializer(instance=note, data=request.data)
        if serializer.is_valid():
            serializer.save()
    elif request.method == "DELETE":
        note.delete()
        return Response("Deleted Successfully")

    return Response(serializer.data)