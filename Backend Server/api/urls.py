from django.urls import path
from . import views

urlpatterns = [
    path("post-event/", views.postEvent, name="post-event"),
    path("post-report/", views.fixReports, name="post-report"),
]