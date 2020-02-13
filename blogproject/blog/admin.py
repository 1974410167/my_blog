from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','create_time','modified_time','category','author']
    fields = ['title','body','excerpt','category','tags']

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request,obj,form,change)

admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
