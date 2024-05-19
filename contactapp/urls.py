from django.urls import path
from . import views


urlpatterns = [
    path('', views.sendMassage, name='send_massage'),
]
