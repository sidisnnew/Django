from . import views
from django.urls import path

app_name = "ticket"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:t_id>/", views.detail, name="detail"),
    path("tickets/", views.ticketlist, name="tickets"),
    path("all/", views.allticketlist, name="all"),
]