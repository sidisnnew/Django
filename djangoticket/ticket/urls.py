from . import views
from django.urls import path

app_name = "ticket"
urlpatterns = [
    path("", views.login, name="login"),
    path("main", views.main, name="main"),
    path("tickets/", views.ticketlist, name="tickets"),
    path("all/", views.allticketlist, name="all"),
    path("<int:t_id>/", views.detail, name="detail"),
    path("logout/", views.logout, name="logout"),
]