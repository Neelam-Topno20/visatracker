from django.db import models
from datetime import datetime


class Role(models.Model):
    role_name = models.CharField(max_length=50)
   # employee = models.ManyToManyField(Employee)

    def __str__(self):
        return self.role_name


class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    manager_id = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    date_created = models.DateTimeField("date created", default=datetime.now())
    date_modified = models.DateTimeField("date modified", default=datetime.now())
    role = models.ManyToManyField(Role)

    def __str__(self):
        return self.first_name





("\n"
 "class EmployeeRoles(models.Model):\n"
 "    role = models.ForeignKey(Role, on_delete=models.CASCADE)\n"
 "    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)\n"
 "    date_created = models.DateTimeField(\"date created\", default=datetime.now())\n"
 "    date_modified = models.DateTimeField(\"date modified\", default=datetime.now())\n")


class ApplicationStatus(models.Model):
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.status


class EmailContent(models.Model):
    content = models.CharField(max_length=500)
    status_id=models.OneToOneField(ApplicationStatus,on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class VisaApplication(models.Model):
    employee_id=models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='employee_id')
    initiated_by = models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='initiated_by',null=True,blank=True)
    status_id=models.ForeignKey(ApplicationStatus,on_delete=models.CASCADE)
    action_pending_on=models.ForeignKey(Employee,on_delete=models.CASCADE,related_name='action_pending_on',null=True,blank=True)
    date_created = models.DateTimeField("date created", default=datetime.now())
    date_modified = models.DateTimeField("date modified", default=datetime.now())



class ApplicationHistory(models.Model):
    application_id=models.ForeignKey(VisaApplication,on_delete=models.CASCADE)
    date_created = models.DateTimeField("date created", default=datetime.now())


class EmailLog(models.Model):
    application_history_id= models.OneToOneField(ApplicationHistory,on_delete=models.CASCADE)
    date_created = models.DateTimeField("date created", default=datetime.now())



