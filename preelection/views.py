from django.shortcuts import render, redirect
from django.http import HttpResponse
from voter.models import Contestant

# Create your views here.
def home(request):
    return render(request, 'home.html')

def candidatesHomePage(request):
    contestants = [
        ('VP', 'VP',Contestant.objects.filter(post='VP').order_by('?')),
        ('HAB', 'HAB',Contestant.objects.filter(post='HAB').order_by('?')),
        ('UGS', 'UG_Senator',Contestant.objects.filter(post='UGS').order_by('?')),
        ('PGS','PG_Senator',Contestant.objects.filter(post='PGS').order_by('?')),
        ('GS','G_Senator',Contestant.objects.filter(post='GS').order_by('?')),
        ('Tech','Technical',Contestant.objects.filter(post='Tech').order_by('?')),
        ('Cult','Cultural',Contestant.objects.filter(post='Cult').order_by('?')),
        ('Welfare','Welfare',Contestant.objects.filter(post='Welfare').order_by('?')),
        ('Sports','Sports',Contestant.objects.filter(post='Sports').order_by('?')),
        ('SAIL','SAIL',Contestant.objects.filter(post='SAIL').order_by('?')),
        ('SWC','SWC',Contestant.objects.filter(post='SWC').order_by('?')),
    ]
    ## tagline
    # Name
    # agendas text
    ## agendas pdf link
    ## video
    # {% url 'homepage' 'VP' %}
    return render(request, 'homepage.html',{'candidates':contestants})