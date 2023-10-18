from django.shortcuts import render
import pymysql
from django.views.decorators.csrf import csrf_exempt
from HELLO_MEM.dao_mem import DaoMem

def mem_list(request):
    dm = DaoMem()
    mems = dm.selectList()
    return render(request, 'mem_list.html', {'mems' : mems })

def mem_detail(request):
    dm = DaoMem()
    m_id = request.GET.get('m_id')
    mem = dm.selectOne(m_id)
    return render(request, 'mem_detail.html', {'mem' : mem})

def mem_mod(request):
    dm = DaoMem()
    m_id = request.GET.get('m_id')
    mem = dm.selectOne(m_id)
    return render(request, 'mem_mod.html', {'mem' : mem})

@csrf_exempt
def mem_mod_act(request):
    dm = DaoMem()
    m_id = request.POST.get('m_id')
    m_nm = request.POST.get('m_nm')
    tel = request.POST.get('tel')
    address = request.POST.get('address')
    
    cnt = dm.update(m_id, m_nm, tel, address)
    
    return render(request, "mem_mod_act.html",{'cnt' : cnt})
        
        
def mem_del(request):
    dm = DaoMem()
    m_id = request.GET.get('m_id')
    cnt = dm.delete(m_id)
    
    return render(request, "mem_del_act.html", {'cnt' : cnt})


def mem_add(request):
    return render(request, "mem_add.html")

def mem_add_act(request):
    dm = DaoMem()
    m_id = request.POST.get('m_id')
    m_nm = request.POST.get('m_nm')
    tel = request.POST.get('tel')
    address = request.POST.get('address')
    
    cnt = dm.insert(m_id, m_nm, tel, address);
    return render(request, "mem_add_act.html",{'cnt' : cnt})
    