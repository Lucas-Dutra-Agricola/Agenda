from django.urls import path
from compromisso import views

app_name = 'compromisso'

urlpatterns = [
    path('',views.index, name='index'),
]
