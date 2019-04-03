from django.contrib import admin

# Register your models here.
from .models import Userdata

class UserdataAdmin(admin.ModelAdmin):
    list_display = ('userid', 'age', 'spiral', 'tremor', 'questionnaire', 'prediction')
    list_filter = ('prediction',)
    search_fields = ('userid',)
    list_per_page = 25

admin.site.register(Userdata, UserdataAdmin)