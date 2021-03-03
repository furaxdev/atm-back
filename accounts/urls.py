from django.urls import path

from . import views

urlpatterns = [
    path('getuawe',views.index , name='get user')
]