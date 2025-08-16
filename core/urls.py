from django.urls import path
from core.views import student_login, index, check_result, my_result, student_logout


app_name ='core'

urlpatterns = [
    path("", index, name='index'),
    path("login", student_login, name='login'),
    path("logout", student_logout, name='logout'),
    path('check-results/', check_result, name='check_result'),
    path('my-result/<int:session_id>/<int:semester_id>/', my_result, name='result_page'),
    
    
]