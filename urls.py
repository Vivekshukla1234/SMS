from django.urls import path
from .views import *


urlpatterns = [
   path('pay/',PaymentDetails),
   path('stu/',get_stu_by_course_name),
   path('stufrm/',get_Studentfrm),
   path('payfrm/',get_Paymentfrm),
   path('static/',get_static),
   path('stuimg/<int:sid>/',veiw_student_by_image),
]
