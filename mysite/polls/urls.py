from django.urls import path

from . import views

urlpatterns = [
    # http://localhost:8000/polls/ のアクセス先
    path("", views.index, name="index"),
]
