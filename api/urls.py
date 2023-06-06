from django.urls import path

from . import views

urlpatterns = [
    path("task", views.index, name="index"),
    path("create", views.create_user, name="create"),
    path("tasks", views.user_tasks, name="user"),
    path("login", views.logeo, name="login"),
    path("user", views.user, name="getuser"),
    path("logout", views.logout_view, name="logout")
]