from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Room, Topic
from .forms import RoomForm

# Create your views here.
def registerLogin(request):
    if request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')
                 
       user = authenticate(request, username=username, password=password)
      
       if user is not None:
          login(request, user)
          messages.success(request, "Welcome")
          return redirect('home')
       else:
          messages.error(request, "username or password is incorrect")
    context = {}
    return render(request, 'register_login.html', context)

def logoutView(request):
    logout(request)
    return redirect('home')

def home(request):
    q = request.GET.get('q') if request.GET.get('q')!= None else ''
    rooms = Room.objects.filter(Q(topic__topic__icontains=q) | Q(description__icontains=q) |  Q(name__icontains=q))
    topics = Topic.objects.all()
    room_count = rooms.count()
    context = {'rooms': rooms, 'topics': topics, 'room_count': room_count}
    return render(request, 'home.html', context)


def room(request,pk):
    room = Room.objects.get(id=pk)
    return render(request, 'room.html', {'room': room})

@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
          form.save()
          return redirect('home')
    return render(request, 'create_room.html', {'form': form})


@login_required(login_url='login')
def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
          form.save(request.POST)
          return redirect('home')
    return render(request, 'update_room.html', {'form': form})


@login_required(login_url='login')
def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'delete_room.html', {'room': room})


