from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


from django.contrib.auth.models import BaseUserManager

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    objects = CustomUserManager()
    avatar = models.ImageField(null=True, default="avatar.svg")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']  # Add any additional required fields here

    def __str__(self):
        return self.email

class Song(models.Model):
    title = models.CharField(max_length=200 , null=True , blank=True)
    artist = models.CharField(max_length=200 , null=True , blank=True)
    file = models.FileField(upload_to='song_file/' , null=True , blank=True)
    avatar = models.ImageField(null=True, default='avatar.svg', blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title}-{self.artist}"
class Topic(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
class Room(models.Model):
    host=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    topic=models.ForeignKey(Topic,on_delete=models.SET_NULL,null=True)
    songs = models.ForeignKey('Song', on_delete=models.CASCADE , null= True)
    name=models.CharField(max_length=255)
    participants=models.ManyToManyField(User,related_name='participants',blank=True)
    description=models.TextField(null=True,blank=True)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering=['-updated','-created']
class Message(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    body=models.TextField()
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']


    def __str__(self):
        return self.body[0:10]
