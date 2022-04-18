from django.contrib import admin

from .models import Blog


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ['thumbnail','title', 'author', 'edited_date']


admin.site.register(Blog, BlogAdmin)
