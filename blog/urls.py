from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='bhome'),
    path('<int:blog_id>/',views.post, name='detail'),
]
