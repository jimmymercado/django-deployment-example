from django.shortcuts import render
from django.http import HttpResponse
from test_app.models import User
from test_app.forms import NewUserForm

# Create your views here.

def home(req):
    #return HttpResponse('home')
    dict = {'test_data': 'Welcome to my Python/Django site!'}
    return render(req, 'test_app/home.html', context=dict)

def index(req):
    return HttpResponse('index')

def test(req):
    return HttpResponse('test')

def help(req):
        #return HttpResponse('home')
    dict = {'data': 'Welcome to my Support and Help page!'}
    return render(req, 'test_app/help.html', context=dict)


def users(req):
    user_list = User.objects.all()
    user_dict = {'userlist':user_list}
    return render(req,'test_app/users.html', context=user_dict)

def signup(req):
    form = NewUserForm()

    if req.method == "POST":
        form = NewUserForm(req.POST)    

        if form.is_valid():
            form.save(commit =True)
            return home(req)
        else:
            print('error in form')

    return render(req, 'test_app/signup.html', {'form': form })