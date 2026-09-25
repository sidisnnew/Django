from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Ticket
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def main(request):
    ticket_number = Ticket.objects.filter(t_status=False).count()
    all_ticket_number = Ticket.objects.count()
    context = {"ticket_number":ticket_number, "all_ticket_number":all_ticket_number}
    return render(request, "ticket/main.html", context)


@login_required
def ticketlist(request):
    if request.user.is_authenticated:
        ticket_list = Ticket.objects.filter(t_status=False).order_by("pub_date")
        context = {"ticket_list":ticket_list}
        return render(request, "ticket/ticket_list.html", context)
    else:
        return HttpResponseRedirect("/ticket")


@login_required
def allticketlist(request):
    if request.user.is_authenticated:
        all_ticket_list = Ticket.objects.order_by("-pub_date")
        context = {"all_ticket_list":all_ticket_list}
        return render(request, "ticket/all_ticket_list.html", context)
    else:
        return HttpResponseRedirect("/ticket")


@login_required
def detail(request, t_id):
    if request.user.is_authenticated:
        ticket = get_object_or_404(Ticket, pk=t_id)
        context = {"ticket":ticket}
        return render(request, "ticket/detail.html", context)
    else:
        return HttpResponseRedirect("/ticket")


def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect("/ticket/main")
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect("/ticket/main")
    else:
        return render(request, "ticket/login.html", locals())


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/main")