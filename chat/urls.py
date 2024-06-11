from django.urls import path
from .views import chatGpt

urlpatterns = [
    path('', chatGpt, name='chatGpt'),

]