from django.contrib import admin
from .models import  Room,Topic,Message,User,Song
# Register your models here.
admin.site.register(Room)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'body', 'created', 'updated')
admin.site.register(Topic)
admin.site.register(User)
admin.site.register(Message,MessageAdmin)
admin.site.register(Song)



