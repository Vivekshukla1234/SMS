from django.db import models

# Create your models here.

class Student22(models.Model):

    name=models.CharField(max_length=50,null=False,blank=False)
    age=models.IntegerField()
    mobileno=models.CharField(max_length=30,null=False,blank=False)
    dob=models.DateField(null=True,blank=True)
    pic=models.ImageField(null=True,blank=True)
    created_by=models.DateTimeField(null=True,blank=True,auto_now_add=True)
    modified_by=models.DateTimeField(null=True,blank=True,auto_now=True)

    def __str__(self):
        return self.name
    

class Course22(models.Model):
    name=models.CharField(max_length=60,blank=False,null=False)

    students=models.ManyToManyField(Student22,null=True,blank=True)
    def __str__(self):
        return self.name
    
class PaymentDetails(models.Model):
    amount=models.IntegerField()
    payment_mode=models.CharField(max_length=30,choices=[('DEBIT CARD','debit card'),
    ('CREDIT CARD','crebit card'),('PAYTM CARD','Paytm card'),('CASH','cash')])
    payment_date=models.DateTimeField(auto_now=True)
    student22=models.ForeignKey(Student22,null=False,blank=False,on_delete=models.CASCADE)





