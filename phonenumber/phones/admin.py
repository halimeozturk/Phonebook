from django.contrib import admin

from .models import Phone_Number, Group
import datetime
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name',)

class Phone_NumberAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'phone_number', 'group')
    list_filter = ('group',)
    list_select_related = ('group',)


admin.site.register(Phone_Number, Phone_NumberAdmin)
admin.site.register(Group, GroupAdmin)
