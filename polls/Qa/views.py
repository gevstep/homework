from django.shortcuts import render
from .models import Quastion, Choice
from django.http import HttpResponse

def detail(request, quastion_id):
    my_list = []
    quastion = Quastion.objects.get(pk=quastion_id)
    choice = Choice.objects.filter(quastion=quastion_id)
    for object in choice:
        my_list.append('<br>' + object.choice_text + " " + str(object.votes))

    return HttpResponse(quastion.quastion_text + ''.join(my_list))
