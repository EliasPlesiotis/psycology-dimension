from django.urls import path

from . import views


urlpatterns = [
    path(r'', views.questionnaires.as_view(), name='questionnaires'),
    path(r'search/', views.questionnaire_search.as_view(), name='questionnaire_search'),
    path(r'<slug:pk>', views.questionnaire.as_view(), name='questionnaire'),
    path(r'<slug:pk>/read', views.questionnaire_read.as_view(), name='questionnaire_read')
]