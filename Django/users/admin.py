from users.models import Profile
""" User admin classes."""
#django
from django.contrib import admin

# Models
from users.models import Profile

# de esta forma tambien se puede agregar un modelo
#admin.site.register(Profile)

@admin.register(Profile)
class profileAdmin(admin.ModelAdmin):
    """Profile admin."""
    list_display = ('pk','user','phoneNumber', 'website','picture')
    list_display_links = ('pk', 'user')
    list_editable = ('phoneNumber',)
    search_fields = ('user__email','user__phoneNumber')
