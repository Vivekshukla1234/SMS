from django.shortcuts import render
from django.http import HttpResponse
from SMS.models import *
from .forms import Studentforms22,PaymentDetailsforms22
# Create your views here.

def PaymentDetails(request):
    if request.method=="GET":
        resp=render(request,'SMS/pmtdetails.html')
        return resp
    
    elif request.method=="POST":
        sid=int(request.POST.get('txtsid',0))
        s1=Student22.objects.get(id=sid)
        allpay=s1.paymentdetails_set.all()
        d1={"allp":allpay,'stu':s1}
        resp=render(request,'SMS/pmtdetails.html',context=d1)
        return resp
    

def get_stu_by_course_name(request):

    Course=Course22.objects.all()
    d1={'course':Course}

    if request.method=='GET':
        cid=Course22.objects.get(id=7)
        d1['courseid']=cid.id
        d1['cname']=cid.name  

        allcou=cid.students.all()
        d1['alval']=allcou
        resp=render(request,'SMS/student.html',context=d1)
        return resp

 
    elif request.method=='POST':
        crid=int(request.POST.get('crid',0))
        cid=Course22.objects.get(id=crid)
        d1['courseid']=cid.id
        d1['cname']=cid.name 
        allcou=cid.students.all()
        d1['alval']=allcou
        resp=render(request,'SMS/student.html',context=d1)
        return resp
    


def get_Studentfrm(request):
    if request.method=='GET':
        
        un_bound=Studentforms22()
        d1={'forms':un_bound}
        resp=render(request,'SMS/stdfrm.html',context=d1)
        return resp

    elif request.method=='POST':
        frm_bound=Studentforms22(request.POST,request.FILES)
        if frm_bound.is_valid():
            frm_bound.save()
    
            resp=HttpResponse('<h1>Student register Successfully </h1>')
            return resp
        
        else:
            d1={'forms':frm_bound}
            resp=render(request,'SMS/stdfrm.html',context=d1)
            return resp
        

def get_Paymentfrm(request):
    if request.method=='GET':
        
        un_bound=PaymentDetailsforms22()
        d1={'forms':un_bound}
        resp=render(request,'SMS/payfrm.html',context=d1)
        return resp

    elif request.method=='POST':
        frm_bound=PaymentDetailsforms22(request.POST)
        if frm_bound.is_valid():
            frm_bound.save()
        
            resp=HttpResponse('<h1>Payment Successfully completed>>> </h1>')
            return resp
        
        else:
            d1={'forms':frm_bound}
            resp=render(request,'SMS/payfrm.html',context=d1)
            return resp
        

def get_static(request):
    resp=render(request,'SMS/static.html')
    return resp



def veiw_student_by_image(request,sid):
    stid=Student22.objects.get(id=sid)
    d1={'stu':stid}
    resp=render(request,'SMS/stuimg.html',context=d1)
    return resp
