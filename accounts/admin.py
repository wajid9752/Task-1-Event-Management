from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class UserAccountAdmin(UserAdmin):
    list_display=('email','is_active')
    search_fields=('email',)
    readonly_fields=('id',)
    ordering = ('email',)  # Specify a valid field for ordering
    fieldsets=(
        ('Personal',
            {
                'fields':('email','first_name','last_name')
            }),
            ('Permissions', {'fields': (
            'groups','user_permissions',
            )}),
            )

admin.site.register(CustomUser , UserAccountAdmin) 
