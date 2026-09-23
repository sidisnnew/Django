from django.db import models

# Create your models here.
class ticket(models.Model):
    t_title = models.CharField(max_length=100)
    t_content = models.CharField(max_length=500)
    pub_date = models.DateTimeField("Date published")
    t_status = models.BooleanField(default=False)