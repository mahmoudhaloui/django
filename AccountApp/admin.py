from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Doctor, Patient, Speciality

admin.site.register(User, UserAdmin)
admin.site.register(Speciality)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['license_number']
        return []


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['national_id']
        return []