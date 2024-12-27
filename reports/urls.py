from unicodedata import name
from django.urls import path
from . import views

urlpatterns=[
    path('',views.login_stu,name='login_stu'),
    path('login_stu',views.login_stu,name='login_stu'),
    path('login_fac',views.login_fac,name='login_fac'),
    path('registration_stu',views.registration_stu,name='registration_stu'),
    path('registration_faculty',views.registration_faculty,name='registration_faculty'),
    path('final_report',views.final_report,name='final_report'),
    path('final_report_fac',views.final_report_fac,name='final_report_fac'),
    path('registration',views.registration,name='registration'),
    path('submit_review1', views.submit_review1, name='submit_review1'),
    path('submit_review2', views.submit_review2, name='submit_review2'),
    path('submit_review3', views.submit_review3, name='submit_review3'),

]