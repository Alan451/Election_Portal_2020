from celery import shared_task
import time
from celery_progress.backend import ProgressRecorder
from voter.models import Voter,Contestant
from django.contrib.auth.models import User
from .decrypt import decryptCipherText
from .models import notaCount
from .backup import backup_votes
positions=['vp','hab','tech','cult','sports','welfare','sail','swc','bsen','gsen']
post_dictionary = {
    'vp':'VP',
    'hab':'HAB',
    'tech':'Tech',
    'cult':'Cult',
    'welfare':'Welfare',
    'sports':'Sports',
    'sail':'SAIL',
    'swc':'SWC',
    'gsen':'GS',      
}
def vote_count(vote,cat,dicti):
  k=vote.split(',')
  for i in range (10):
    if i>=8:
      x=k[i].split(':')[1].strip()
      if x == 'NOTA':
        if i==8:
          nota = cat
        else:
          nota = ' NOTA'
        if nota in dicti[positions[i]]:
          dicti[positions[i]][nota] += 1
        else:
          dicti[positions[i]][nota] = 1
      else:  
        y=x[1:-1].split()
        for j in y:
          if (j in dicti[positions[i]]):
            dicti[positions[i]][j]=dicti[positions[i]][j]+1
          else: dicti[positions[i]][j]=1  
    else:  
      x=k[i].split(':')
      # print(x[1])
      if (x[1] in dicti[positions[i]]):
        dicti[positions[i]][x[1]]=dicti[positions[i]][x[1]]+1
      else: 
        dicti[positions[i]][x[1]]=1

@shared_task(bind=True)
def do_work(self):
    notaCount.objects.all().delete()
    dicti={}
    for i in positions:
      dicti[i]={}
    progress_recorder = ProgressRecorder(self)
    voters = Voter.objects.all().filter(final_submit=True)
    for i in range(len(voters)):
        # print(voters[i])
        # backup_votes(voters[i].vote_string1, voters[i].vote_string2, voters[i].vote_time)
        vote_string = decryptCipherText(voters[i].vote_string1,voters[i].vote_time)+decryptCipherText(voters[i].vote_string2,voters[i].vote_time)
        # print(vote_string)
        if voters[i].category == '0' or voters[i].category == '1':
          cat= 'UGS'
        else:
          cat = 'PGS'
        vote_count(vote_string,cat,dicti)
        progress_recorder.set_progress(i+1,len(voters),description="Decrypting... ")
    for post in dicti:
        for key in dicti[post]:
            try:
                pk = int(key)
                cont=Contestant.objects.get(pk=pk)
                cont.vote_count = dicti[post][key]
                cont.save()
            except:
                if key == ' NOTA':
                  try:
                    notaCount.objects.create(post=post_dictionary[post],vote_count=dicti[post][key])
                  except:
                    nota = notaCount.objects.get(post=post_dictionary[post])
                    nota.vote_count= dicti[post][key]
                    nota.save()
                elif key=='UGS' or key=='PGS':
                  try:
                    notaCount.objects.create(post=key,vote_count=dicti[post][key])
                  except:
                    nota = notaCount.objects.get(post=key)
                    nota.vote_count= dicti[post][key]
                    nota.save()
                        
    return "Work Completed"