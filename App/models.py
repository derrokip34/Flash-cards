from django.db import models
from django.contrib.auth.models import User
from django import forms

# Create your models here.
class Subject(models.Model):
    subject = models.CharField(max_length=30)

    def __str__(self):
        return self.subject

    def save_subject(self):
        self.save()

class FlashCard(models.Model):
    card_title = models.CharField(max_length=50)
    card_notes = models.CharField(max_length=250)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE)
    posted_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.card_title

    def save_card(self):
        self.save()

    def delete_card(self):
        self.delete()
