from django.contrib import admin
from .models import Ticket, Comment, TicketImage

# Register your models here.
admin.site.register(Ticket)
admin.site.register(Comment)
admin.site.register(TicketImage)