from django.urls import path

from . import views


urlpatterns = [
    path(r'register/', views.register.as_view(), name='register'),
    path(r'id/', views.get_id.as_view(), name='get_id')
]