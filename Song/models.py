from django.db import models

# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    artist = models.CharField(max_length=200, null=True, blank=True)
    file = models.FileField(upload_to='song_file/', null=True, blank=True)
    avatar = models.ImageField(null=True, default='avatar.svg', blank=True)
    # creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title}-{self.artist}"