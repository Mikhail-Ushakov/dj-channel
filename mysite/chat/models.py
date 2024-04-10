from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Chats(models.Model):
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User)
    

class Messeges(models.Model):
    user = models.ForeignKey(User, models.SET_NULL, null=True)
    text = models.TextField()
    # file = models.FileField(upload_to='chat_files/', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    chat = models.ForeignKey(Chats, related_name='messeges', on_delete=models.CASCADE)