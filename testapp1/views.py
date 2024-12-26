from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from django.views.generic import View

# Create your views here.
def emp_data_view(request):
    emp_data ={
    'eno' : 101,
    'ename' : 'Sunny',
    'esal' : 12000,
    'eaddr' : 'Mumbai'
    }
    resp = '<h1>Employee Number:{}<br>Employee Name:{}<br>Employee Salary:{}<br>Employee Address:{}</h1>'.format(emp_data['eno'],emp_data['ename'],emp_data['esal'],emp_data['eaddr'])
    return HttpResponse(resp)

def emp_data_jsonview(request):
    emp_data ={
    'eno' : 102,
    'ename' : 'Bunny',
    'esal' : 15000,
    'eaddr' : 'Hyd'
    }
    json_data = json.dumps(emp_data)
    return HttpResponse(json_data)

def emp_data_jsonview2(request):
    emp_data ={
    'eno' : 103,
    'ename' : 'Vinny',
    'esal' : 18000,
    'eaddr' : 'Vja'
    }
    return JsonResponse(emp_data) # Pretty-print format of MongoDB available

class JsonCBV(View):
    def get(self,request,*args,**kwargs):
        emp_data ={
        'eno' : 104,
        'ename' : 'Radhika',
        'esal' : 22000,
        'eaddr' : 'Chennai'
        }
        return JsonResponse(emp_data)
