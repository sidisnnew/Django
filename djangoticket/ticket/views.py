from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Index")

def ticketlist(request):
    return HttpResponse("List")

def allticketlist(request):
    return HttpResponse("All")

def detail(request, t_id):
    return HttpResponse("Detail %s" % t_id)