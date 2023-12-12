from django.shortcuts import render
from django.http import HttpResponse
from main.models import Company,Employee
from django.db.models import Count
from django.http import HttpResponseRedirect

# Create your views here.


def companies_view(request):

    companies_with_employees = Company.objects.prefetch_related('employee_set')
    return render(request, 'companies.html', {"companies_with_employees":companies_with_employees })


def employees_view(request,com_pk):
    employees=Employee.objects.all()
    return render(request,'employees.html',{'employees':employees,'com_pk':com_pk})

def employees_add(request):
    if request.method == 'POST':
        try:
            emp_id = request.POST.get('employee')
            com_id = request.POST.get('company_id')
            employee = Employee.objects.get(pk=emp_id)
            company = Company.objects.get(pk=com_id)
        
        # Check if the employee is already linked to a company
            if employee.company:
                # Unlink the employee from their current company
                employee.company = None
                employee.save()
        
        # Link the employee to the new company
            employee.company = company
            employee.save()
            return HttpResponseRedirect('/')
        except:
            return HttpResponse('Please Select Company and Employee!! ')
    return HttpResponse('Please Select Company and Employee!! ')
