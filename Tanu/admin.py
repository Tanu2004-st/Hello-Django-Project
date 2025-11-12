from django.contrib import admin
from Tanu.models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email','phone', 'desc','date')

# Register your models here.
admin.site.register(Contact,ContactAdmin)
#password:tanu123@
#username:admin