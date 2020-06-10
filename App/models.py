from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FlashCard(models.Model):
    card_title = models.CharField(max_length=50)
    card_notes = models.CharField(max_length=250)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
