from django.shortcuts import render
from django.http import HttpResponse
from .models import person
# Create your views here.

def index (request): 
    person1 = person()
    person1.name = 'Fernandinho'
    person1.beroep = 'Mechanical Engineer'
    person1.beschrijving = 'Ijverig en leergierig'
    person1.img = 'user1.jpg'
    person1.bol = False

    person2 = person()
    person2.name = 'Alejandro'
    person2.beroep = 'Software developer'
    person2.beschrijving = 'super slim'
    person2.bol = True


    person3 = person()
    person3.name = 'Serkan'
    person3.beroep = 'Software engineer'
    person3.beschrijving = 'Mucho experienco'
    person3.bol = True

    return render(request, 'index.html', {'person1': person1, 'person2': person2,'person3': person3})




