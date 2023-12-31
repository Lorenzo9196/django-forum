from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    topic = models.CharField(max_length=100)

    def  __str__(self):
        return self.topic

    
class Room(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,  null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL,  null=True)
    name = models.CharField(max_length=100)
    participants = models.ManyToManyField(User, related_name="participants", blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now_add=True)

    def  __str__(self):
        return self.name
    
class  Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    message = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message[0:50]
    
