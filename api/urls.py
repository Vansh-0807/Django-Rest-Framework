from home.views import index, person, course, color, login, PersonAPI
from django.urls import path

urlpatterns = [
    path('index/', index),
    path('person/', person),
    path('course/', course),
    path('color/', color),
    path('login/', login),
    path('persons/', PersonAPI.as_view())
]