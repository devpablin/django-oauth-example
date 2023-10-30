
from django.urls import re_path
from .views import (
    TodoListApiView, UserDetails,UserDetailsFree,
)

urlpatterns = [
    re_path('api', TodoListApiView.as_view()),
    re_path('users', UserDetails.as_view()),
    re_path('free', UserDetailsFree.as_view()),
]