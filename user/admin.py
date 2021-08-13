from django.contrib import admin
from . import models
from django.contrib.auth.models import Group
from django.utils.translation import gettext as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

class UserAdmin(BaseUserAdmin):
    list_display = ('firstname', 'lastname', 'phone_number', 'is_staff', 'paid_till')
    list_filter = ('is_staff',)
    fieldsets = ((None, {'fields': ('phone_number', 'firstname', 'lastname', 'password', 'paid_till')}),
        # (_('Personal Info'),{'fields': ('id', )}),
        (
            _('Permissions'),
            {
                'fields': ('is_active', 'is_staff', 'is_superuser',)
            }
        ),
        (_('Important Dates'), {
            'fields': ('last_login', )
        }),
    )
    add_fieldsets = (
        (None, {'classes': ('wide'),
                'fields': ('firstname',
                           'lastname',
                           'phone_number',
                           'password1',
                           'password2',
                           'paid_till')
                }),
    )
    search_fields = ('phone_number',)
    ordering = ('phone_number', )

admin.site.register(models.Region)
admin.site.register(models.User)
admin.site.unregister(Group)
