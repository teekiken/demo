# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('Hello World!')

def guizi(request):
    return HttpResponse('Hello Baby!')

def hello(request):
    return render(request,'hello.html')  #返回hello.html模板


def xuan_ran(request):
    return render(request,'pass.html',context={"name":"郑桂贤"})  #返回hello.html模板