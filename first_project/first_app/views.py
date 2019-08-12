from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic, Website, AccessRecord

# Create your views here.

def index(req):
    #return HttpResponse('<h1>Main View!</h1>')
    dict = {'insert_me':'text from def index(req) views.py!'}
    return render(req, 'first_app/index.html', context=dict)


def hello(req):
    return HttpResponse('<h1>Hello World from Django!</h1>')


def first_app(req):
    return HttpResponse('<h1>My First Django App!</h1>')


def viewlist(req):
    weblist = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': weblist}

    return render(req, 'first_app/viewlist.html', context=date_dict)

    