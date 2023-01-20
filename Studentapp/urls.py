from django.urls import path

from Studentapp import views

urlpatterns=[
            path('',views.log_fun,name='log'),#it will display login,html page
            path('logdata',views.logdata_fun),
            path('reg',views.reg_fun,name='reg'),#return to register.html page
            path('regdata',views.regdata_fun),#it will create superuser account
            path('home',views.home_fun,name='home'),#it will redirect to home.html

            path('add_students',views.addstudent_fun,name='add'),
            path('readdata',views.readdata_fun),#it will insert record into studenttable
            path('display',views.display_fun,name='display'),
            path('update/<int:id>',views.update_fun,name='update'),
            path('del/<int:id>',views.delete_fun,name='del'),
            path('log_out',views.log_out_fun,name='log_out'),
]