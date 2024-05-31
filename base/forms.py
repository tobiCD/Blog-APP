from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from .models import Room, User, Song


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username','email', 'password1', 'password2']


class RoomForm(ModelForm):
    class Meta:
        model=Room
        fields= ['topic', 'name', 'description', 'songs']
        exclude=['host']

    def __init__(self, *args, **kwargs):
        super(RoomForm, self).__init__(*args, **kwargs)
        self.fields['songs'].queryset = Song.objects.all()

class UserForm(ModelForm):
    class Meta:
        model= User
        fields =['avatar','name','username','email']
        # gọi các fields trong form gọi ra manf hình

class SongForm(ModelForm):
    class Meta:
        model= Song
        fields= '__all__'
