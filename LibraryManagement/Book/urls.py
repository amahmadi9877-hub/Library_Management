from django.urls import path
from django.shortcuts import redirect
from Book.views import book_list, book_detail, book_create_update

urlpatterns = [
    path('detail/<int:pk>', book_detail, name="book_detail" ),
    path('update/<int:pk>', book_create_update, name="book_update" ),
    path('create/', book_create_update, name="book_create"),
    path('list/',book_list, name="book_list" ),
    path('',lambda _ : redirect("book_list"), name="book_default" ),
]