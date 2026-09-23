from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Ticket

# Create your views here.
def index(request):
    return HttpResponse("Index")

def ticketlist(request):
    ticket_list = Ticket.objects.filter(t_status=False).order_by("pub_date")
    output = ", ".join([t.t_title for t in ticket_list])
    return HttpResponse(output)

def allticketlist(request):
    all_ticket_list = Ticket.objects.order_by("-pub_date")
    output = ", ".join(t.t_title for t in all_ticket_list)
    return HttpResponse(output)

def detail(request, t_id):
    ticket = get_object_or_404(Ticket, pk=t_id)
    output = ticket.t_content
    return HttpResponse(output)