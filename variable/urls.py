from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.variables.as_view(), name='varibles'),
    path(r'<slug:pk>', views.variable.as_view(), name='variable')
]