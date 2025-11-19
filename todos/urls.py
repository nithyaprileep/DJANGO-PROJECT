
from django.urls import path
from .views import (
    register_user,
    login_user,
    TodoListCreateAPIView,
    TodoRetrieveUpdateDeleteAPIView
)

urlpatterns = [
    path("register/", register_user, name="register"),
    path("login/", login_user, name="login"),
    path("todos/", TodoListCreateAPIView.as_view(), name="todo-list-create"),
    path("todos/<int:pk>/", TodoRetrieveUpdateDeleteAPIView.as_view(), name="todo-detail"),
]