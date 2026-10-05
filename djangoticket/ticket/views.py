from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Ticket, Comment
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
    ticket_list = Ticket.objects.filter(t_status=False).order_by("pub_date")
    context = {"ticket_list":ticket_list}
    return render(request, "ticket/ticket_list.html", context)


@login_required
def allticketlist(request):
    from_date = request.GET.get("from")
    to_date = request.GET.get("to")

    all_ticket_list = Ticket.objects.order_by("-pub_date")
    if from_date and to_date:
        all_ticket_list = all_ticket_list.filter(
            pub_date__range=[from_date, to_date]
        )
    elif from_date:
        all_ticket_list = all_ticket_list.filter(
            pub_date__gte=from_date
        )
    elif to_date:
        all_ticket_list = all_ticket_list.filter(
            pub_date__lte=to_date
        )

    context = {"all_ticket_list":all_ticket_list}
    return render(request, "ticket/all_ticket_list.html", context)


@login_required
def detail(request, t_id):
    ticket = get_object_or_404(Ticket, pk=t_id)
    comments = Comment.objects.filter(ticket=ticket).order_by("pub_date")
    if request.method == "POST":
        action = request.POST.get("action")
        if action == "status":
            ticket.t_status = not ticket.t_status
            ticket.save()
        elif action == "comment":
            content = request.POST.get("comment")
            Comment.objects.create(ticket=ticket, content=content)

    context = {"ticket":ticket, "comments":comments}    
    return render(request, "ticket/detail.html", context)


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
    return render(request, "ticket/logout.html")