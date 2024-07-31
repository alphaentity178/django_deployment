from django.shortcuts import render
from Login_app.forms import UserForm , UserInfoForm
from Login_app.models import UserInfo
from django.contrib.auth.models import User

from django.contrib.auth import authenticate , login , logout
from django.http import HttpResponseRedirect , HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.


def login_page(request) :
    diction = {}
    return render(request , 'Login_app/login.html' , context=diction)
   
def user_login(request) :

    diction = {}

    if request.method == 'POST' :
        uername = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = uername , password = password)

        if user :
            if user.is_active :
                login(request , user)
                return HttpResponseRedirect(reverse('Login_app:index'))
            else :
                return HttpResponse("Account is not ative!")
            
        else :
            return HttpResponse('Ligin details are wrong!')
        
    else :
        HttpResponseRedirect(reverse("Login_app:login_apge"))
        
    
@login_required
def user_logout(request) :
    logout(request)
    return HttpResponseRedirect(reverse("Login_app:index"))


def index(request) :

    diction = {}

    if request.user.is_authenticated :
        current_user = request.user
        user_id = current_user.id 
        user_base_info = User.objects.get(pk = user_id)
        user_more_info = UserInfo.objects.get(user__pk = user_id)
        diction = {'user_base_info': user_base_info , 'user_more_info': user_more_info}

    return render(request , 'Login_app/index.html' , context=diction)


def register(request) :

    registered = False

    if request.method == 'POST' :
        user_form = UserForm(data=request.POST)
        user_info_form = UserInfoForm(data=request.POST)

        if user_form.is_valid() and user_info_form.is_valid() :
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            user_info = user_info_form.save(commit=False)
            user_info.user = user

            if 'profile_pic' in request.FILES :
                user_info.profile_pic = request.FILES['profile_pic']

            user_info.save()
            registered = True

    else :
        user_form = UserForm()
        user_info_form = UserInfoForm()

    diction = {'user_form' : user_form , 'user_info_form' : user_info_form , 'registered' : registered}

    return render(request , 'Login_app/register.html' , context=diction)
