from django.contrib import admin
from .models import ClientIntake

class ClientIntakeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'gender', 'age', 'phone_number', 'diet_type', 'training_frequency')
    search_fields = ('full_name', 'phone_number', 'diet_type')
    list_filter = ('gender', 'diet_type', 'training_frequency')

admin.site.register(ClientIntake, ClientIntakeAdmin)
