from django.contrib import admin
from .models import *
# Register your models here.
class TutorAdmin(admin.ModelAdmin):
    list_display = ('name', 'topic', 'course','date',)
    search_fields = ('name', 'topic',)
    date_hierarchy = 'date'


admin.site.register(Tutor, TutorAdmin)
admin.site.register(Study)
admin.site.register(SemesterCategory)
admin.site.register(StudyCourse)