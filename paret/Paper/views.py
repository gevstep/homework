from django.shortcuts import render
from .models import User_input
# Create your views here.

def paret_paper(request):
     my_object = User_input.objects.all()[0]
     date_for_print = my_object.today_date
     user_name_for_print = my_object.user_name
     exit_time_for_print = my_object.exit_time
     exit_address_for_print = my_object.exit_address
     visit_address_for_print = my_object.visit_address
     visit_purpose_for_print = my_object.visit_purpose
     return_time_for_print = my_object.return_time
     my_dict = {'date': date_for_print, 'user_name': user_name_for_print, 'exit_time': exit_time_for_print, 'exit_address': exit_address_for_print, 'visit_address': visit_address_for_print, 'visit_purpose': visit_purpose_for_print, 'return_time': return_time_for_print}
     print(date_for_print)
     return render(request, 'Paper/first_page.html', my_dict)
