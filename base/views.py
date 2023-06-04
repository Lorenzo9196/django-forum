from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm

# Create your views here.
def home(request):
     rooms = Room.objects.all()
     return render(request, 'home.html', {'rooms': rooms})


def room(request,pk):
     room = Room.objects.get(id=pk)
     return render(request, 'room.html', {'room': room})

def createRoom(request):
     form = RoomForm()
     if request.method == 'POST':
          form = RoomForm(request.POST)
          if form.is_valid():
              form.save()
              return redirect('home')
     return render(request, 'create_room.html', {'form': form})

def updateRoom(request,pk):
     room = Room.objects.get(id=pk)
     form = RoomForm(request.POST, instance=room)
     if request.method == 'POST':
          form = RoomForm(request.POST, instance=room)
          if form.is_valid():
              form.save(request.POST, instance=room)
              return redirect('home')
     return render(request, 'update_room.html', {'form': form})

def deleteRoom(request,pk):
     room = Room.objects.get(id=pk)
     if request.method == 'POST':
          room.delete()
          return redirect('home')
     return render(request, 'delete_room.html', {'room': room})


