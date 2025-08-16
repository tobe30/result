from django.contrib import admin
from core.models import Student, Course, Semester, Session, Result

# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('reg_number', 'name', 'password')
    
class SessionAdmin(admin.ModelAdmin):
    list_display = ('name')
    
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('name')

class ResultAdmin(admin.ModelAdmin):
    list_display = ('student','session','semester')
    
admin.site.register(Student, StudentAdmin)
admin.site.register(Course)
admin.site.register(Session)
admin.site.register(Semester)
admin.site.register(Result, ResultAdmin)

