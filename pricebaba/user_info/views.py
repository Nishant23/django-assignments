from django.shortcuts import render
from .models import users
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime
from django.http import JsonResponse
from django.core import serializers
import json
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext

def index(request):
    user = users.objects.all()
    paginator = Paginator(user, 5)
    page = request.GET.get('page')
    try:
        _users = paginator.page(page)
    except PageNotAnInteger:
        _users = paginator.page(1)
    except EmptyPage:
        _users = paginator.page(paginator.num_pages)
    return render(request, "index.html", {'users': _users})

def addUser(request):
    return render(request, "user_info/add_user.html", {'fn':"", 'ln':"", 'emi':"", 'mn':"", 'a':"", 'dob':"", 'l':"",'met':"Add"})

def Add(request):
    if request.POST:
        response_data = {}
        _id = request.session['id']
        fn = request.POST.get('first_name')
        ln = request.POST.get('last_name')
        emi = request.POST.get('email')
        mn = request.POST.get('mobile')
        a = request.POST.get('age')
        dob = request.POST.get('dob')
        loc = request.POST.get('location')
        query = users(first_name = fn, last_name = ln, email_id = emi, mobile = mn, age = a, date_of_birth = dob, place = loc)
        query.save()
        response_data['redirect'] = '/'
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

def edit(request, pk):
    query = users.objects.filter(pk = pk)
    fn, ln, emi, mn, a, dob, l = "", "", "", "", "", "", ""
    for q in query:
        fn = q.first_name
        ln = q.last_name
        emi = q.email_id
        mn = q.mobile
        a = q.age
        dob = q.date_of_birth
        l = q.place
        _id = q.id
        request.session['id'] = _id
        return render(request, "user_info/add_user.html", {'fn':fn, 'ln':ln, 'emi':emi, 'mn':mn, 'a':a, 'dob':dob, 'l':l,'met':"Update"})

def Update(request):
    if request.POST:
        response_data = {}
        print request.POST.get('email')
        _id = request.session['id']
        fn = request.POST.get('first_name')
        ln = request.POST.get('last_name')
        emi = request.POST.get('email')
        mn = request.POST.get('mobile')
        a = request.POST.get('age')
        dob = request.POST.get('dob')
        loc = request.POST.get('location')
        query = users.objects.filter(pk = _id).update(first_name = fn, last_name = ln, email_id = emi, mobile = mn, age = a, date_of_birth = dob, place = loc)
        response_data['redirect'] = '/'
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
