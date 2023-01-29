from django.urls import path
from .views import (
    UserView,
)

urlpatterns = [
    path('add_user/', UserView.as_view()),
    path('add_user/<int:pk>/', UserView.as_view()),
]