from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path("index", views.index),
    path("post", views.post),
    path("aboutme", views.aboutme),
    path("feedback", views.feedback, name="feedback"),
]