from django import forms 
from SMS.models import Student22,PaymentDetails

class Studentforms22(forms.ModelForm):
    class Meta:
        model=Student22
        fields='__all__' #['name','age','mobileno']


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        for fld in self.fields.values():
            fld.widget.attrs['placeholder']='Enter your ' + fld.label


class PaymentDetailsforms22(forms.ModelForm):
    class Meta:
        model=PaymentDetails
        fields='__all__'