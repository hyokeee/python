from django.shortcuts import render
import pymysql
from HELLO_EMP.dao_emp import DaoEmp
from django.views.decorators.csrf import csrf_exempt

def emp_list(request):
    de = DaoEmp()
    emps = de.selectList()
    return render(request, 'emp_list.html', {'emps' : emps })

def emp_list_fake(request):
    de = DaoEmp()
    emps = de.selectList()
    return render(request, 'emp_list_fake.html', {'emps' : emps })

def emp_detail(request):
    de = DaoEmp()
    e_id = request.GET.get('e_id')
    emp = de.selectOne(e_id)
    return render(request, 'emp_detail.html', {'emp' : emp})

def emp_mod(request):
    de = DaoEmp()
    e_id = request.GET.get('e_id')
    emp = de.selectOne(e_id)
    return render(request, 'emp_mod.html', {'emp' : emp})

@csrf_exempt
def emp_mod_act(request):
    de = DaoEmp()
    e_id = request.POST.get('e_id')
    e_name = request.POST.get('e_name')
    gen = request.POST.get('gen')
    addr = request.POST.get('addr')
    
    cnt = de.update(e_id, e_name, gen, addr)
    
    return render(request, "emp_mod_act.html",{'cnt' : cnt})
        
        
def emp_del(request):
    de = DaoEmp()
    e_id = request.GET.get('e_id')
    cnt = de.delete(e_id)
    
    return render(request, "emp_del_act.html", {'cnt' : cnt})


def emp_add(request):
    return render(request, "emp_add.html")

def emp_add_act(request):
    de = DaoEmp()
    e_id = request.POST.get('e_id')
    e_name = request.POST.get('e_name')
    gen = request.POST.get('gen')
    addr = request.POST.get('addr')
    
    cnt = de.insert(e_id, e_name, gen, addr);
    return render(request, "emp_add_act.html",{'cnt' : cnt})
    