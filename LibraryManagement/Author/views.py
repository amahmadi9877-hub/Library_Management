from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def author_list(request: HttpRequest) -> HttpResponse:
    return HttpResponse("form author_list")

def author_detail(request: HttpRequest, pk: str) -> HttpResponse:
    return HttpResponse("form author_detail")

def author_create_update(request: HttpRequest) -> HttpResponse:
    return HttpResponse("form author_create_update")