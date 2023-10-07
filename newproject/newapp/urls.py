from django.urls import path
from . import views

urlpatterns = [
    path('', views.esports_page, name="esports_page"),
]