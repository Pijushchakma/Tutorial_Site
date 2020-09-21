from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
Status = [
    ('NotStarted','Not Started'),
    ('Started','Started'),
    ('Completed','Completed')
]

class Category(models.Model):
    CatName = models.CharField(max_length=20)
    def __str__(self):
        return self.CatName
class Course(models.Model):
    name = models.CharField(max_length=50)
    descriptionCourse = RichTextField(blank=True,null=True)
    CatName = models.ForeignKey('Category',on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('content',kwargs={
            'id':self.id
        })    
class CourseContent(models.Model):
    Coursename = models.CharField(max_length=50)
    ContentName = models.CharField(max_length=30)
    descriptionContent = RichTextField(blank=True,null=True)
    content = RichTextField(blank=True,null=True)
    order = models.IntegerField()
    isFree = models.BooleanField(default=False)
    def __str__(self):
        return self.ContentName
    def get_absolute_url(self):
        return reverse('contentdetails',kwargs={
            'id':self.id
        })     
class UserDetails(models.Model):
    user = models.CharField(max_length=20)
    course = models.CharField(max_length=50)
    status = models.CharField(max_length=20,default='Not Started')

    def __str__(self):
        return self.user


class track(models.Model):
    userName = models.CharField(max_length=20)
    courseName = models.CharField(max_length=50)
    now = models.IntegerField(default=0)
    def __str__(self):
        return self.courseName
