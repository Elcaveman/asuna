from django.contrib import admin
from django.contrib.auth.admin import Group, UserAdmin
from .models import Patient

class PatientAdmin(UserAdmin):
    #you can add groups if you need to
    fieldsets = (('Personnal Info',{'fields':('client_name','email','password')}),
    ('Permissions',{'fields':(('is_active','is_staff','is_superuser'),'user_permissions')}),
    ('Extra information',{'fields':('weight','is_male','is_smoker', 'is_pregnant', 'is_obese')}),
    ('Important Dates',{'fields':(('date_joined','last_login','birthday'))}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('client_name','email', 'password1', 'password2'),
        }),
    )
    list_display = ('email','client_name' ,'date_joined','is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    search_fields = ('email', 'client_name')
    ordering = ('email',)

    filter_horizontal = ('user_permissions',)
    readonly_fields = ('date_joined','last_login')

admin.site.register(Patient,PatientAdmin)