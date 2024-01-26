from django.urls import path
from .views import *

urlpatterns = [
    path("", getRoutes, name="routes"),
    path("note/", getNotes, name="notes"),
    path("note/<str:pk>/", getNote, name="note"),
]