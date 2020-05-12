from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from . import views

app_name = 'books'

urlpatterns = [
    #url(r'^$',views.IndexView.as_view(), name='index'),
    path('', views.IndexView.as_view(), name='index'),

    #/books/book_id/
    path('<int:pk>', views.DetailView.as_view(), name='detail'),
    path('books/add/', views.BookCreate.as_view(), name='book-add'),
]