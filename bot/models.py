from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# class Event(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField(blank=True)
#     start_date = models.DateTimeField(null=True)


class MessagesCount(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    stupid_count=models.IntegerField(default=0)
    fat_count=models.IntegerField(default=0)
    dump_count=models.IntegerField(default=0)

    def __str__(self):
        return self.user.username