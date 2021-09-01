from django.urls import path

from .views import Twitter

urlpatterns = [
    path('', Twitter.as_view()),
]
