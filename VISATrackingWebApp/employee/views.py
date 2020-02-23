from django.shortcuts import render
from .models import Employee


# Create your views here.
def homepage(request):
    return render(request, 'main/employees.html', context={"employees": Employee.objects.all})
