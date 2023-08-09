from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('create/', views.create_book, name='create_book'),
    path('list/', views.list_books, name='list_books'),
    
]
