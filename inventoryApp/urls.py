from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('create/', views.create_book, name='create_book'),
    path('list/', views.list_books, name='list_books'),
    path('update/<int:pk>/', views.update_book, name='update_book'),
    path('delete/<int:pk>/', views.delete_book, name='delete_book'),
    
]
