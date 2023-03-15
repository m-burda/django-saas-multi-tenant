from django.urls import path, include

urlpatterns = [
    path('api/', include('restaurant.urls')),
    path('users/', include('rest_framework.urls')),
    path('users/', include('users.urls')),
]
