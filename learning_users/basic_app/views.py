from django.shortcuts import render
from basic_app import models, forms

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(req):
    pHeader = {'page_header': 'This is the Index Page'}
    return render(req, 'basic_app/index.html', context=pHeader )




def register(req):
    pHeader = {'page_header': 'This is the Registration Page'}
    

    registered = False

    if req.method == "POST":
        userform = forms.UserForm(data=req.POST)
        profileform = forms.UserProfileInfoForm(data=req.POST)
    
        if userform.is_valid() and profileform.is_valid():
            user = userform.save()
            user.set_password(user.password)
            user.save()

            profile = profileform.save(commit=False)
            profile.user = user

            if 'profile_pic' in req.FILES:
                profile.profile_pic = req.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(userform.errors, profileform.errors)

    else:
        userform = forms.UserForm()
        profileform = forms.UserProfileInfoForm()

    return render(
        req, 
        'basic_app/registration.html', 
        {'page_header':'This is the Registration Page', 'registered': registered, 'UserForm': userform, 'UserProfileForm': profileform}
    )

def user_login(req):

    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        

        user = authenticate(req, username=username, password=password)

        if user:
            if user.is_active:
                    login(req, user)
                    return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Account inactive!')

        else:
            print('Someone tried to login and failed!')
            print(f'Username: {username}')
            return HttpResponse('invalid login details!')

    else:
        return render(req, 'basic_app/login.html', {})

@login_required
def user_logout(req):
    logout(req)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special_page(req):
    return HttpResponse('you\'re logged in, nice!')