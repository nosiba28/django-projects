from django.shortcuts import render, get_object_or_404, redirect
from .forms import CreateEmployeeForm
from .models import Employee


# from django.views.generic import (UpdateView)

def Home(request):
    employees = Employee.objects.all().order_by("-emp_id")
    context = {'employees': employees}
    return render(request, 'index.html', context)


def CreateEmployee(request):
    if request.method == "POST":
        form = CreateEmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            # form = CreateEmployeeForm()
            # return render(request, 'index.html', context)
            return redirect(Home)

    else:
        form = CreateEmployeeForm()

    employees = Employee.objects.all().order_by("-emp_id")
    context = {'form': form, 'employees': employees}
    return render(request, 'addnew.html', context)


def GetEmployee(request, **kwargs):
    id = kwargs.get('id')
    employee = get_object_or_404(Employee, emp_id=id)
    if request.method == "POST":
        form = CreateEmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect(Home)
    else:
        form = CreateEmployeeForm(instance=employee)

    context = {'employee': employee, 'form': form}
    return render(request, 'emp_edit.html', context)


# class GetEmployee(UpdateView):
#     model = Employee
#     form_class = EditForm
#     template_name = 'emp_edit.html'


def DeleteEmployee(request, **kwargs):
    id = kwargs.get('id')
    employee = Employee.objects.get(emp_id=id)
    employee.delete()
    return redirect(Home)
