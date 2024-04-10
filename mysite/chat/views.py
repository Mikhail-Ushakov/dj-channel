from django.shortcuts import render
from .models import Chats

def index(request):
    chats = Chats.objects.all()
    return render(request, "chat/index.html", {'chats': chats})


def room(request, room_name):
    chat = Chats.objects.get_or_create(name=room_name)
    chat.users.add(request.user)
    chat.save()
    return render(request, "chat/room.html", {"room_name": room_name, 'chat': chat})