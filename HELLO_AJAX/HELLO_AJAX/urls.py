from django.contrib import admin
from django.urls import path
from HELLO_AJAX import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', views.emp),
    path('emp', views.emp),
    path('ajax', views.ajax),
    path('emp_list', views.emp_list),
    path('emp_one', views.emp_one),
    path('emp_del_ajax', views.emp_del_ajax),
    path('emp_add_ajax', views.emp_add_ajax),
    path('emp_mod_ajax', views.emp_mod_ajax),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)