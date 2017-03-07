from django.contrib import admin
from django.core.mail import send_mail

from .models import users

def send_email(modeladmin, request, queryset):
    for user in queryset:
       send_mail('Welcome-to-Bioinfo-Workshop','Good-Day','rajeshs@cdac.in',[user.email],
                           fail_silently=False,)
    send_email.short_description = "Say Hi to all Users"

class UsersList(admin.ModelAdmin):
    fields = ['name', 'email', 'birthdate', 'reg_date', 'group', 'slot']
    list_display = ('name', 'reg_date', 'group', 'slot')
    search_fields = ['name']
    actions = [send_email]

admin.site.register(users, UsersList)

