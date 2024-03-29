from django.urls import path
from .views import *

urlpatterns = [
    path("", getRoutes, name="routes"),
    path("note/", getNotes, name="notes"),
    path("note/<str:pk>/", handleNote, name="note"),
    path("register/", registerUser, name="register"),
    path("login/", loginUser, name="login"),
    path("user/", getUser, name="user"),
    path("logout/", logoutUser, name="logout"),
]