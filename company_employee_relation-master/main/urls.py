from django.urls import path

from main import views

app_name = 'api'

urlpatterns = [
    path('', views.companies_view),
    path('employees/<int:com_pk>',views.employees_view,name='employees'),
    path('employee_add/',views.employees_add,name='employee_add')

]
