from django.urls import path
from .views import HelloWorldApiView

urlpatterns = [
    path('', HelloWorldApiView.as_view(), name='hello_world')
]
