from django.urls import path

from apps.reviews import views

urlpatterns = [
    path('books/', views.book_list, name='book_list')
]
