from django.urls import path
from .views import *

urlpatterns = [
    path('livres/', getBooks),
    path('add/', addBook),
    path('update/<int:id>', updateBook),
    path('delete/<int:id>', deleteBook),


]
