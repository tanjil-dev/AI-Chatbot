from django.urls import path
from chatbot.views import chatbot

urlpatterns = [
    path('', chatbot, name ='chatbot')
]