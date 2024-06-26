from django.contrib import admin

from students.models import Subject


# Register your models here.
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    list_filter = ('title',)

