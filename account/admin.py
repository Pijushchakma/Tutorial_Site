from django.contrib import admin
from .models import Course,UserDetails,CourseContent,Category,track
admin.site.register(Course)
admin.site.register(UserDetails)
admin.site.register(CourseContent)
# admin.site.register(AllCourses)
admin.site.register(Category)
admin.site.register(track)
# Register your models here.
