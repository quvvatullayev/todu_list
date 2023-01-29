from django.urls import path
from .views import (
    UserView,
    UserUpdate,
    DeleteUser,
)

urlpatterns = [
    path('add_user/', UserView.as_view()),
    path('add_user/<int:pk>/', UserView.as_view()),
    path('user_update/<int:pk>/', UserUpdate.as_view()),
    path('delete_user/<int:pk>/', DeleteUser.as_view())
]