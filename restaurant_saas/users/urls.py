from django.urls import path

from . import views

urlpatterns = [
    path('', views.UserListAPIView.as_view()),
    path('<int:pk>', views.RetrieveUserModelAPIView.as_view())
]