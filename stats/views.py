# from typing import final
from django.db.models.expressions import Random
from django.shortcuts import render
from voter.models import Voter
from django.db.models import Q
from django.http import JsonResponse
import random
# Create your views here.
deptList =[
    'CSE',
    'ECE',
    'ME',
    'Civil',
    'Design',
    'BSBE',
    'CL',
    'EEE',
    'Physics',
    'Chemistry',
    'MNC',
    'HSS',
    'Energy',
    'Environment',
    'Nano-Tech',
    'Rural-Tech',
    'Linguistics',
]

hostelDicti = {
    '0':'HOSTEL NOT ALLOTED',
    '1':'BRAHMAPUTRA',
    '2':'DHANSIRI',
    '3':'DIBANG',
    '4':'DIHING',
    '5':'DISANG',
    '6':'KAMENG',
    '7':'KAPILI',
    '8':'LOHIT',
    '9':'MANAS',
    '10':'MARRIED SCHOLARS HOSTEL',
    '11':'SIANG',
    '12':'SUBHANSIRI',
    '13':'UMIAM',
    '14':'BARAK',
}

def deptFetchData():
    deptCount = {}
    jagrukDept = 0
    data = {}
    for j,i in enumerate(deptList):
        total = Voter.objects.filter(dept = i).count()
        count = Voter.objects.filter(Q(dept=i) & Q(final_submit=True)).count()
        deptCount[i] = {'count':count,'total':total,'percent':round((count*100)/total,2)}
        if deptCount[i]['percent'] > jagrukDept and j<12:
            jagrukDept = deptCount[i]['percent']  
            data['jagrukDept']=i
    data['deptCount'] = deptCount
    return data

def hostelFetchData():
    hostelCount = {}
    jagrukHostel = 0
    data = {}
    for i in range(15):
        total = Voter.objects.filter(hostel = str(i)).count()
        count = Voter.objects.filter(Q(hostel = str(i)) & Q(final_submit=True)).count()
        hostelCount[hostelDicti[str(i)]] = {'count':count}
        if hostelCount[hostelDicti[str(i)]]['count'] > jagrukHostel and i!=0:
            jagrukHostel = hostelCount[hostelDicti[str(i)]]['count']
            data['jagrukHostel']=hostelDicti[str(i)]
    data['hostelCount'] = hostelCount
    return data

def totalVotersData():
    data = {}
    # defaultCoords=25
    totalVoted = Voter.objects.filter(final_submit = True).count()
    data['totalVoted'] = [ i for i in f'{totalVoted:04}']
    totalVoters = Voter.objects.all().count()
    data['totalVotedCount'] = totalVoted
    # if totalVoted <=25:
    #     defaultCoords=totalVoted
    # data['coords'] = random.sample([[coords[0].x,coords[0].y] for coords in Voter.objects.filter(final_submit=True).values_list('voter_location')], defaultCoords)
    percent = (totalVoted*100)//totalVoters
    data['votePercent'] = [ i for i in f'{percent:02}']
    data['coords'] = [[coords[0].x,coords[0].y] for coords in Voter.objects.filter(final_submit=True).values_list('voter_location')]
    return data    

def percent():
    data ={}
    totalUg = Voter.objects.filter(Q(category=0) | Q(category=1)).count()
    #  & Q(final_submit=True)
    ugVoted = Voter.objects.filter(Q(category=0) | Q(category=1)).filter(final_submit=True).count()
    ugPercent = (ugVoted/totalUg)*100
    totalPg = Voter.objects.filter(Q(category=2) | Q(category=3)).count()
    PgVoted = Voter.objects.filter(Q(category=2) | Q(category=3)).filter(final_submit=True).count()
    pgPercent = (PgVoted/totalPg)*100
    totalBoys = Voter.objects.filter(Q(category=2) | Q(category=0)).count()
    totalGirls = Voter.objects.filter(Q(category=1) | Q(category=3)).count()
    BoysVoted = Voter.objects.filter(Q(category=0) | Q(category=2)).filter(final_submit=True).count()
    GirlsVoted = Voter.objects.filter(Q(category=1) | Q(category=3)).filter(final_submit=True).count()
    data['completeStats'] = {
        'totalUg': totalUg,
        'totalPg': totalPg,
        'totalBoys': totalBoys,
        'totalGirls': totalGirls,
        'ugVoted': ugVoted,
        'PgVoted':PgVoted,
        'BoysVoted':BoysVoted,
        'GirlsVoted': GirlsVoted,
        'ugPercent': ugPercent,
        'pgPercent': pgPercent
    }
    return data
def voteData(request):
    data = {}
    data.update(percent())
    data.update(totalVotersData())
    data.update(deptFetchData())
    data.update(hostelFetchData())
    
    # print(data['coords'])
    return JsonResponse(data)


def stats(request):
    return render(request,'stats.html',{})


























































































































































































































































































































