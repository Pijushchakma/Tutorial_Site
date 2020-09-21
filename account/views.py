from django.shortcuts import render, redirect, get_object_or_404, reverse, HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Category, Course, UserDetails, CourseContent, track

# Create your views here.


def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user_name = request.POST['user_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(first_name=first_name).exists():
                messages.info(request, 'User Name already exist')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exist')
                return redirect('register')
            else:
                user = User.objects.create_user(
                    username=user_name, first_name=first_name, last_name=last_name, email=email, password=password1)
                user.save()
                auth.login(request, user)
                return redirect('index')
        else:
            messages.info(request, 'Password Does Not Match ')
            return redirect('register')
    else:
        return render(request, 'registration.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
def contact(request):
    return render(request,'contact.html')
def profile(request):
    l = list()
    allCourses = UserDetails.objects.filter(user = request.user.username)
    num = UserDetails.objects.filter(user = request.user.username).count()
    for coun in range(num):
        print(allCourses[coun].course)
        courses = Course.objects.filter(name = allCourses[coun].course)
        l.append(courses[0])

    context = {
        'allCourses':allCourses,
        'num':num,
        'l':l,
    }
    return render(request,'profile.html',context)    
def AddCourse(request):
    l = list()
    category = Category.objects.all()
    courses = Course.objects.all()
    for cour in courses:
        Status = UserDetails.objects.filter(
            user=request.user.username, course=cour.name)
        if Status:
            l.append(Status[0].status)
        else:
            l.append("not listed")
    context = {
        'category': category,
        'courses': courses,
        'l': l
    }
    return render(request, 'Addcourse.html', context)


def extraadd(request):
    name = request.GET['name']
    course = Course.objects.filter(id=name)
    baal = UserDetails.objects.all()
    if UserDetails.objects.filter(user=request.user.username, course=course[0].name).exists():
        print('exist')
        
    else:
        use = UserDetails.objects.create(
            user=request.user.username, course=course[0].name)
        use.save()
        
        Track = track.objects.create(
            userName=request.user.username, courseName=course[0].name)
        Track.save()

        return HttpResponse('True')

def Content(request, id):
    content = get_object_or_404(Course, id=id)
    content = Course.objects.filter(id=id)
    Track = track.objects.filter(
        userName=request.user.username, courseName=content[0].name)
    details = CourseContent.objects.filter(
        Coursename__icontains=content[0].name).order_by('order')
    totalContent = CourseContent.objects.filter(
        Coursename__icontains=content[0].name).count()
    sequal = Track[0].now +1   
        
    context = {
        'content': content,
        'details': details,
        'sequal':sequal,
        'totalContent':totalContent
    }
    return render(request, 'dashboard.html', context)

def Contentdetails(request, id):
    content = get_object_or_404(CourseContent, id=id)
    
    Track = track.objects.filter(
        userName=request.user.username, courseName=content.Coursename)
    mark = 0    
    if content.order == Track[0].now:
        mark = 1    
    nowValue = Track[0].now + 1
    if content.order < nowValue:
        context = {
            'content': content,
            'mark':mark
        }
        return render(request, 'contentDetails.html', context)
    else:
        context = {
            'message': 'Please Read Sequentially'
        }
        return render(request,'contentDetails.html',context)

def increase(request):
    name = request.GET['name']
    userStatus = UserDetails.objects.filter(user=request.user.username,course=name).update(status='Started')
    Track = track.objects.filter(
        userName=request.user.username, courseName=name)
    nowValue = Track[0].now + 1
   
    track.objects.filter(userName=request.user.username,
                         courseName=name).update(now=nowValue)
   
    return HttpResponse('True')
def dashboard(request):
    return render(request,'dashboard.html')
def StatusChange(request):
    name = request.GET['name']
    val = request.GET['val']
    
    val = val + '%' + '  Completed'
    print(val)
    userStatus = UserDetails.objects.filter(user=request.user.username,course=name).update(status=val)
    return HttpResponse('True')
