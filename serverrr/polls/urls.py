
from django.urls import path

from polls.views import question_list

app_name = 'polls'

urlpatterns = [
    path('', question_list, name='question_list'),
]
