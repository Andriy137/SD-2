
from django.urls import path

from polls.views import question_list, register_view

app_name = 'polls'

urlpatterns = [
    path('', question_list, name='question_list'),
    path('register/', register_view, name='register')
]
