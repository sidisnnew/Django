from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Ticket

# Create your views here.
def index(request):
    ticket_number = Ticket.objects.filter(t_status=False).count()
    all_ticket_number = Ticket.objects.count()
    context = {"ticket_number":ticket_number, "all_ticket_number":all_ticket_number}
    return render(request, "ticket/index.html", context)

def ticketlist(request):
    ticket_list = Ticket.objects.filter(t_status=False).order_by("pub_date")
    context = {"ticket_list":ticket_list}
    return render(request, "ticket/ticket_list.html", context)

def allticketlist(request):
    all_ticket_list = Ticket.objects.order_by("-pub_date")
    context = {"all_ticket_list":all_ticket_list}
    return render(request, "ticket/all_ticket_list.html", context)

def detail(request, t_id):
    ticket = get_object_or_404(Ticket, pk=t_id)
    context = {"ticket":ticket}
    return render(request, "ticket/detail.html", context)