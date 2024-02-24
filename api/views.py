from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import *
from .models import *
import jwt, datetime
from .utils import *
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
# Create your views here.

@api_view(["GET"])
def getRoutes(request):
    routes = [
        "GET /note",
        "GET /note/:id"
    ]
    return Response(routes)

@api_view(["GET", "POST"])
def getNotes(request):
    token = request.COOKIES.get('jwt')
    payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    user = User.objects.filter(id=payload['id']).first()
    print(payload['id'])
    print(user)
    print("Hello how ar e")
    if request.method == "POST":
        Notes.objects.create(title=request.data['title'], body=request.data['body'], user=user)
    notes = Notes.objects.filter(user=user).order_by("-updated")
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

@api_view(["POST"])
def registerUser(request):
    username = request.data["username"]
    password1 = request.data["password1"]
    password2 = request.data["password2"]
    try:
        validate_custom_username(username)
        validate_custom_password(password1)
        if password1 != password2:
            raise ValidationError("Password does not match")
    except ValidationError as e:
        return Response(e)
    hashed_password = make_password(password1)
    user = User.objects.create(username=username, password=hashed_password)
    payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

    token = jwt.encode(payload, 'secret', algorithm='HS256')

    response = Response()
    response.set_cookie(key='jwt', value=token, httponly=True)
    response.data = {'jwt': token, "py": payload}

    return response

@api_view(["POST"])
def loginUser(request):
    username = request.data["username"]
    password = request.data["password"]
    print(username)
    print(password)
    try:
        user = authenticate(request, username=username, password=password)
        if user is not None:
            payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
            }

            token = jwt.encode(payload, 'secret', algorithm='HS256')

            response = Response()
            response.set_cookie(key='jwt', value=token, httponly=True)
            response.data = {'jwt': token, "py": payload}

            return response
        else:
            raise ValidationError("Invalid Login Credentials")
    except ValidationError as e:
        return Response(e)
    
@api_view(["GET"])
def getUser(request):
    token = request.COOKIES.get('jwt')
    print(token)
    if not token:
        raise AuthenticationFailed("Unauthenticated!")
    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except Exception as e:
        return Response('Unauthenticated!')

    user = User.objects.filter(id=payload['id']).first()
    serializer = UserSerializer(user)
    return Response(serializer.data)

# {
# "username": "Gabriel",
# "password1": "gab123456",
# "password2": "gab123456"
# }