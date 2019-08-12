from django.shortcuts import render
from . import forms

# Create your views here.

def index(req):
    return render(req, 'basicapp/index.html')

def basic_form(req):
    form = forms.FormName()

    if req.method == 'POST':
        form = forms.FormName(req.POST)

        if form.is_valid():
            #do some code here
            print('validation success!')
            print(f'Name {form.cleaned_data["name"]}')
            print(f'Email {form.cleaned_data["email"]}')
        

    return render(req, 'basicapp/form.html', {'form':form}) 