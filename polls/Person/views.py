from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
from datetime import datetime
# Create your views here.
def index(request):
    obj_1 = Person.objects.all()
    my_list = []
    for object in obj_1:
        my_list.append(object.first_name + " "+ object.last_name + '<br>')
    return HttpResponse(''.join(my_list))

def return_my_name(request):
    return HttpResponse("Gevorg")

def my_html(request):

    return render(request, 'Person/index.html')

def exit_paper(request):
    list_for_print = []
    person_base = Person.objects.all()[1]
    list_for_print.append(person_base.first_name)
    list_for_print.append(person_base.last_name)
    person_print = ' '
    person_print = person_print.join(list_for_print)
    today_response = datetime.now()
    my_dict = {'today': today_response, 'person': person_print}
    return render(request, 'Person/exit_paper.html', my_dict)

def test_page(request):
    obj_print = Person.objects.get(first_name='Gevorg')
    name_name = obj_print.first_name
    surname_surname = obj_print.last_name
    dict_nsi = {'name': name_name, 'surname': surname_surname}
    return render(request, 'Person/test_page.html', dict_nsi)
