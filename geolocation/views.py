from django.shortcuts import render, redirect
from django.http import HttpResponse
import json
from voter.models import Voter
import base64
from .forms import FormWithCaptcha
from django.contrib.auth.decorators import login_required
from voter.views import is_valid
import uuid
# from .models import Post
# from .forms import PostForm

@login_required
@is_valid
def save_user_geolocation(request):
    if request.method == 'POST':
        coord = json.loads(request.POST['data'])
        request.session['latitude']=coord['lat']
        request.session['longitude']=coord['long']
        if request.session['latitude'] and request.session['longitude']:
            print('sfdf')
            request.session['location']= True
        print(coord)
    return redirect('captcha')

@login_required
@is_valid    
def save_user_image(request):
    username = request.user.username
    image_name = request.user.last_name + ".png"
    if Voter.objects.all().filter(username=username).exists():
        voter = Voter.objects.get(username=username)
    else:
        return HttpResponse('get the fuck out of here')
    if request.method == 'POST':
        imagebase64= request.POST['imagebase64data']
        try:
            with open("images/voters/"+image_name, "wb") as fh:
                fh.write(base64.b64decode(imagebase64))
            voter.voter_image= "images/voters/"+image_name
            voter.save()
            request.session['image'] = True
        except Exception:
            print('i fucked up')
            return HttpResponse('something went wrong')
        return redirect('captcha')
    else:
        return redirect('captcha')

def home(request):
    return render(request, 'index.html', {})

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

@login_required
@is_valid
def verification(request):
    request.session['ip']=get_client_ip(request)
    y = "student at"
    uid = str(uuid.uuid1()).split('-')
        
    try:
        voter = Voter.objects.get(username = request.user.username)
        hostel = voter.hostel
        dept = voter.dept
        year = 21-int(request.user.last_name[:2])
        if year == 1:
            y = "1st Year"
        elif year == 2:
            y= "2nd year"
        elif year == 3:
            y="3rd year"
        elif year == 4:
            y="4th year"        
    except:
        return redirect('captcha')
    if not request.method=='POST':
        form = FormWithCaptcha()
        return render(request, 'verification.html', {'form': form,'hostel':hostel,'dept':dept,'year':y,'voter_id':uid[0].upper()})
        
    form = FormWithCaptcha(request.POST)
    if form.is_valid():
        print('u are not a robot')
        request.session['human']= True
        return redirect('vote')
    else:
        return redirect('captcha')
    return render(request, 'verification.html', {'form': form,'hostel':hostel,'dept':dept,'year':y,'voter_id':uid[0].upper()})
