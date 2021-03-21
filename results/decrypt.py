
from django.contrib.auth.models import User
from .models import keys
import rsa
import base64
import time
import random
from django.conf import settings
# done_process = False


def xor(byte_text, vote_time):
    random.seed(vote_time)
    n = len(byte_text)
    arr = [random.randint(0, 127) for i in range(n)]
    key = bytearray(arr)
    byte_text = bytes(a ^ b for (a, b) in zip(byte_text, key))
    return byte_text




def decryptCipherText(cipher_text, vote_time):
  users = []
  files=[]
  try:    
    users.append(User.objects.get(username='swc@iitg.ac.in'))
    users.append(User.objects.get(username='elections@iitg.ac.in'))
    users.append(User.objects.get(username='dos@iitg.ac.in'))  

    files.append(keys.objects.get(user = users[0]))
    files.append(keys.objects.get(user = users[1]))
    files.append(keys.objects.get(user = users[2]))
  except :
    print('None was fetched')
  # print('cipher',cipher_text)
  # print('time',vote_time)
  cipher_text = base64.b64decode(cipher_text.encode())
  # users = ['SWC', 'EC', 'CC']
  time_ = float(vote_time)
  time__ = time_//1
  cipher_text = xor(cipher_text, time__)
  for i in range(2, -1, -1):
    with open(settings.MEDIA_ROOT+'/'+str(files[i].private_key), 'rb') as fr:
      pr = rsa.PrivateKey.load_pkcs1(fr.read())
    cipher_text = rsa.decrypt(cipher_text, pr)
  return cipher_text.decode()

