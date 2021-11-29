from django.conf.urls import url
from . import views
urlpatterns = [
    url('curso/nuevo/', views.curso_nuevo, name='curso_nuevo'),
    ]