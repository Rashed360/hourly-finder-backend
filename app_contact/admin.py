from django.contrib import admin

from .models import Contact, Newsletter


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ['phone', 'email', 'subject', 'message', 'report_date']

class NewsletterAdmin(admin.ModelAdmin):
    list_display = [ 'email', 'join_date']

admin.site.register(Contact, ContactAdmin)
admin.site.register(Newsletter, NewsletterAdmin)
