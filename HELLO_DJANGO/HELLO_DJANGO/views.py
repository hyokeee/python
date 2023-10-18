# cat views.py
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render


def hello(request):
        return HttpResponse("Hello world!!!")

def param(request):
        return HttpResponse("param")
    
def get_param(request):
    #menu = request.GET['menu']
    menu = request.GET.get('menu','뇨끼')
    return HttpResponse(menu)

@csrf_exempt
def post(request):
    menu = request.POST.get('menu')
    if not menu:
        menu = '카라멜마끼야또'
    return HttpResponse(menu)

def forw(request):
    a = "홍길동"
    b = ["후쿠시마","오염수","겁나맛있네"]
    c = [
        {'e_id' : '1', 'e_name' : '1', 'gen' : '1', 'addr' : '1',},
        {'e_id' : '2', 'e_name' : '2', 'gen' : '2', 'addr' : '2',},
        {'e_id' : '3', 'e_name' : '3', 'gen' : '3', 'addr' : '3',}
        ]
    return render(request, 'forw.html',{
        'a' : a,
        'b' : b,
        'c' : c
    })
    