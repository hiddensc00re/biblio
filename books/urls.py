from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    
    path('books/new', views.create_book, name="create a book")
]