from datetime import timedelta

from django.core.paginator import Paginator
from django.shortcuts import render , redirect
from django.http import HttpResponse
# Create your views here.
from django.contrib.auth.decorators import login_required
from .models import Room, Topic, User, Message, Song
from .forms import RoomForm ,UserForm ,SongForm
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import authenticate ,login , logout
from .forms import MyUserCreationForm
from django.shortcuts import get_object_or_404
from Song.models import Song
from django.utils import timezone
from django.contrib.auth.decorators import permission_required


# sử dụng mẫu model User để authenticate login page và register
def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exit')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)


def logoutPage(request):
    logout(request)
    return redirect('home')


def Register(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')
    return render(request, 'base/login_register.html', {'form': form})


def home(request):
    q=request.GET.get('q') if request.GET.get('q') != None else ''
    rooms=Room.objects.filter(Q(topic__name__icontains=q)|
                              Q(name__icontains=q)|
                              Q(description__icontains=q))
    topics=Topic.objects.all()
    room_count=rooms.count()
    songs=Song.objects.all()
    room_messages=Message.objects.filter(Q(room__topic__name__icontains=q))
    context={'rooms':rooms ,'topics': topics , 'room_count':room_count ,
             'room_messages':room_messages , 'songs':songs}
    return render(request, 'base/home.html', context)

def room(request,pk):
    room=Room.objects.get(id=pk)
    room_messages= room.message_set.all().order_by('-created')
    # request này mô tả cho việc mình cmt vào bài người khác
    # participant mô tả cho các thành viên mà đã cmt bài mình hiện trên slidebar
    participants=room.participants.all()

    if request.method=='POST':
        message=Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room',pk=room.id)
    context={'room':room , 'room_messages':room_messages ,'participants':participants }
    return render(request,'base/room.html',context)

@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    topics = Topic.objects.all()

    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)

        song_title = request.POST.get('song')
        songs = Song.objects.filter(title=song_title)


        room_name = request.POST.get('name')
        room_description = request.POST.get('description')

        print(f"Topic: {topic_name}, Song: {song_title}, Room Name: {room_name}, Room Description: {room_description}")

        Room.objects.create(
            host=request.user,
            topic=topic,
            name=room_name,
            description=room_description,
        )

        print("Room created successfully")

        return redirect('home')

    context = {'form': form, 'topics': topics}
    return render(request, 'base/room_form.html', context)


@login_required(login_url='login')
def updateRoom(request,pk):
    room=Room.objects.get(id=pk)
    form=RoomForm(instance=room)
    topics=Topic.objects.all()
    songs = Song.objects.all()
    if request.user != room.host :
        return HttpResponse('you are not allowed here')
    if request.method=='POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        room.name=request.POST.get('name')
        room.topic=topic
        room.description=request.POST.get('description')
        room.songs = request.POST.get('songs')
        room.save()
        return redirect('home')
    context={'form':form ,'topics':topics ,'room':room ,'songs':songs}

    return render(request,'base/room_form.html',context)

@login_required(login_url='login')
def deleteRoom(request,pk):
    room = get_object_or_404(Room,id=pk)
    # if Room.objects.filter(id=pk):
    #     room = Room.objects.get(id=pk)
    if request.method=='POST':
        room.delete()
        return redirect('home')
    return render(request,'base/delete.html',{'obj':room})

def delete_message(request,pk):
    message = Message.objects.get(id=pk)
    if request.user != message.user:
        # chỉ cho phép user nào xóa cmt user đó
      return HttpResponse('You are not allowed here')
    if request.method=="POST":
        message.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': message})

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics = Topic.objects.all()
    context = {'user': user, 'rooms': rooms,
               'room_messages': room_messages, 'topics': topics}
    return render(request, 'base/profile.html', context)

@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)
    context = {'form': form}
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()

            return redirect('profile', pk=user.id)
        else:
            messages.success(request, 'Edit is not Valid')

    return render(request, 'base/update-user.html', context)
def topicsPage(request):
    # room_messages=Message.objects.all()
    q=request.GET.get('q') if request.GET.get('q') != None else''
    topics=Topic.objects.filter(name__icontains=q)
    return render(request,'base/topics.html',{'topics':topics})

def activityPage(request):

    room_messages = Message.objects.all()
    return render(request, 'base/activity.html', {'room_messages': room_messages})


def createRoomMusic(request):
    form = SongForm()
    songs = Song.objects.all()

    if request.method == 'POST':
        form = SongForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, 'Song created successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Form submission failed. Please check the data.')
            print(form.errors)
    context = {'form': form, 'songs': songs}
    return render(request, 'base/upload_music.html', context)

# def roomandsong(request):
#     room_form = RoomForm()
#     song_form = SongForm
#     if request.method == 'POST':
#         room_form = RoomForm(request.POST)
#         song_form = SongForm(request.POST , request.FILES)
#
#         if room_form.is_valid() and song_form.is_valid():
#             room = room_form.save()
#             room.host = request.user
#             room.save()
#             song = song_form.save(commit=False)
#             song.room = room
#             song.save()
#             return redirect('home')
#         else:
#             room_form = RoomForm()
#             song_form =SongForm()
#     return render(request , 'base/room_songForm.html', {'room_form':room_form,'song_form':song_form})