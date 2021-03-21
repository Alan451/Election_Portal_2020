from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.
from django.http import HttpResponse
from voter.models import Voter,Contestant
from .models import keys
import rsa
import base64
import time
from .forms import publicKeyUploadForm
import random
from django.contrib.auth.models import User
from .tasks import do_work
from .models import notaCount,taskid
from celery.result import AsyncResult

post_dictionary ={
    'VP':'Vice President',
    'HAB' : 'General Secretary of Hostel Affairs Board',
    'UGS': 'Under Graduate Senator',
    'PGS':'Post Graduate Senator',
    'GS':'Girl Senator',
    'Tech':'General Secretary of Technical Board',
    'Cult':'General Secretary of Cultural Board',
    'Welfare':'General Secretary of Students\' Welfare Board',
    'Sports':'General Secretary of Sports Board',
    'SAIL':'General Seceratry of SAIL',
    'SWC':'General Seceratry of SWC',    
}
users = []

 
def is_authorized(user):
    users.clear()
    try:
        users.append(User.objects.get(username='swc@iitg.ac.in'))
    except:
        print("error in results/views.py")
    try:    
        users.append(User.objects.get(username='elections@iitg.ac.in'))
    except:
        print("error in results/views.py")
    try:    
        users.append(User.objects.get(username='dos@iitg.ac.in'))  
    except:
        print("error 3")
    if user in users:
        return True
    return False

@login_required
@user_passes_test(is_authorized,redirect_field_name="home")
def keyUpload(request):
    publicKeys = keys.objects.filter(pubkey=True).values('user')
    public=[]
    for i in range(len(publicKeys)):
        public.append(User.objects.get(pk=publicKeys[i]['user']).first_name)
    privateKeys = keys.objects.filter(prikey=True).values('user')
    private=[]
    for i in range(len(privateKeys)):
        private.append(User.objects.get(pk=privateKeys[i]['user']).first_name)
    everyOne = []
    for i in range(len(users)):
        everyOne.append(users[i].first_name)
    return render(request,'keyinfo.html',{'public':public,'private':private,'Names':everyOne})
    

@login_required
@user_passes_test(is_authorized,redirect_field_name="home")
def publicKey(request):
    files = request.FILES.get('fileUpload', None)
    if request.method == 'POST' and files is not None:
        try:
            key=keys.objects.get(user = request.user)
            key.public_key = files
            key.pubkey =True
            key.save()
        except:
            keys.objects.create(user=request.user,public_key=files,pubkey=True)
        return redirect('keyUpload')
    return render(request, 'pubKeyupload.html', {'keyType': 'Public'})


@login_required
@user_passes_test(is_authorized,redirect_field_name="home")
def privateKey(request):
    files = request.FILES.get('fileUpload', None)
    if request.method == 'POST' and files is not None:
        try:
            key=keys.objects.get(user=request.user)
        except:
            print("fucked up")
        key.private_key = files
        key.prikey = True
        key.save()
        return redirect('keyUpload')
    return render(request, 'pubKeyupload.html', {'keyType':'Private'})



@login_required
@user_passes_test(is_authorized,redirect_field_name="home")
def results(request):
    if request.method == 'POST':
        return redirect('results_view','VP')
    tasks = taskid.objects.all()
    if len(tasks) == 0:
        task = do_work.delay()
        taskid.objects.create(task_id=task.task_id)
        running = task.task_id
    else:
        running = tasks[0].task_id
        res = AsyncResult(running)
    return render(request, 'results.html', {'task_id':running})   


@login_required
@user_passes_test(is_authorized,redirect_field_name="home")
def results_view(request,post):
    cont = list(Contestant.objects.filter(post=post).values_list('name','vote_count'))
    try:
        nota = notaCount.objects.get(post=post)
        cont.append(('NOTA',nota.vote_count))
    except:
        cont.append(('NOTA',0))
    sum=0
    for i in cont:
        sum+=i[1]
    contList = []
    for i in cont:
        contList.append((i[0],i[1],i[1]*100/sum))
    contList.sort(key = lambda x: x[1])
    contList.reverse()
    return render(request,'results_view.html',{'contestants':contList,'post_display':post_dictionary[post],'sum':sum,'post_list':post_dictionary.keys()})
