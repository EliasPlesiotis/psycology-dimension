from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.questions.as_view(), name='questions'),
    path(r'<slug:pk>', views.question.as_view(), name='questions'),
    path(r'<slug:pk>/read', views.question_read.as_view(), name='question_read'),
    path(r'answer/', views.answer.as_view(), name='answer'),
    path(r'answer/<slug:pk>', views.answer_read.as_view(), name='answer_read')
]