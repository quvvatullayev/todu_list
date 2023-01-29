from django.urls import path
from .views import (
    UserView,
    UserUpdate,
    DeleteUser,
    CreteTodu,
    RedeTodo,
    UpdeteTodo,
    DeleteTodo,
)

urlpatterns = [
    path('add_user/', UserView.as_view()),
    path('add_user/<int:pk>/', UserView.as_view()),
    path('user_update/<int:pk>/', UserUpdate.as_view()),
    path('delete_user/<int:pk>/', DeleteUser.as_view()),
    path('add_todo/', CreteTodu.as_view()),
    path('raede_todo/<int:user_id>/', RedeTodo.as_view()),
    path('updete_todo/<int:pk>/', UpdeteTodo.as_view()),
    path('delete_todo/<int:pk>/', DeleteTodo.as_view()),
]