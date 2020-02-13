from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):

    #后台显示的字段
    list_display = ['name','email','url','post','created_time']
    #需要填写的字段
    fields = ['name','email','url','text','post']

admin.site.register(Comment,CommentAdmin)
