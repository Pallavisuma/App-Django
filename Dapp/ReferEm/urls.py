from django.urls import path
from .  import views


urlpatterns = [
   
    path('frm/',views.employee_form,name ='employee_insert'),
    path('<int:id>/',views.employee_form,name= 'update'),
    path('LogIn/',views.auth_login,name= 'auth_login'),
     path('list/',views.employee_list,name= 'employee_list'),
    path('pupdate/',views.pupdate,name= 'pupdate'),
    path('jd/',views.jd,name= 'jd'),
    path('LogOut/',views.lgout,name= 'lgout'),
    path('SignUp/',views.signup,name= 'signup'),
    path('fpass/',views.fpass,name= 'fpass'),
    path('uppdf/',views.uppdf,name= 'uppdf'),
    path('delete/<int:id>/',views.employee_delete,name='employee_delete'),
 
]