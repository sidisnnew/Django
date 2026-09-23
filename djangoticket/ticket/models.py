from django.db import models

# Create your models here.
class Ticket(models.Model):
    t_title = models.CharField(max_length=100)
    t_content = models.CharField(max_length=500)
    pub_date = models.DateTimeField("Date published")
    t_status = models.BooleanField(default=False)
    t_warranty = models.BooleanField(null=True, blank=True, default=None)

    def was_done(self):
        return self.t_status

    def __str__(self):
        return self.t_title