from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def book_list(request: HttpRequest) -> HttpResponse:
    return HttpResponse("form book_list")

def book_detail(request: HttpRequest, pk: str) -> HttpResponse:
    return HttpResponse("form book_detail")

def book_create_update(request: HttpRequest) -> HttpResponse:
    return HttpResponse("form book_create_update")