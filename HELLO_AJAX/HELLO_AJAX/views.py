from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import json
from HELLO_AJAX.dao_emp import DaoEmp

def emp(request):
    return render(request,"emp.html")

@csrf_exempt
def ajax(request):
    data = json.loads(request.body)
    print(data['e_id'])
    print(data.get('e_id'))
    flag = "ok"
    a = {'flag' : flag,
         'flag2' : "ook",
         'data' : data
        }
    return JsonResponse(a)


@csrf_exempt
def emp_list(request):
    de = DaoEmp()
    emps = de.selectList()
    
    #return JsonResponse(list(emps), safe=False)
    return JsonResponse({'list' : emps})

@csrf_exempt
def emp_one(request):
    de = DaoEmp()
    param = json.loads(request.body)
    vo = de.selectOne(param['e_id'])
    return JsonResponse({'vo' : vo})

@csrf_exempt
def emp_del_ajax(request):
    de = DaoEmp()
    data = json.loads(request.body)
    e_id = data['e_id']
    cnt = de.delete(e_id)
    return JsonResponse({'cnt' : cnt})

@csrf_exempt
def emp_mod_ajax(request):
    de = DaoEmp()
    data = json.loads(request.body)
    e_id = data['e_id']
    e_name  = data['e_name']
    gen = data['gen']
    addr = data['addr']
    cnt = de.update(e_id, e_name, gen, addr)
    return JsonResponse({'cnt' : cnt })

@csrf_exempt
def emp_add_ajax(request):
    param = json.loads(request.body)
    e_id = param['e_id']
    e_name  = param['e_name']
    gen = param['gen']
    addr = param['addr']
    de = DaoEmp()
    cnt = de.insert(e_id, e_name, gen, addr)
    
    mydict = {
        'cnt' : cnt
    }
    return JsonResponse(mydict)
