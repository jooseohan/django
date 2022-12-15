from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('predict/', views.predict, name='predict'),
    path('predict/result/', views.result, name='result'),
    path('heart/', views.heart, name='heart'),
    path('heart/run/', views.run, name='run'),
    path('predict/', views.predict, name='predict'),
    path('hospital/', views.hospital, name='hospital'),
    # path('hospital/question_detail', views.question, name='question'),
    path('work/<int:question_id>/', views.question, name='question'),
    path('work/answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('hospital/question_create/', views.question_create, name='question_create'),
]