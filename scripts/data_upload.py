import csv
import random
from django.utils.encoding import smart_str
from voter.models import Contestant, Voter
from django.contrib.gis.geos import Point

CHARS = "abcdefghjkmnpqrstuvwxyABCDEFGHJKLMNPQRSTUVWXY3456789"

deptList ={
    '01': 'CSE',
    '02': 'ECE',
    '03': 'ME',
    '04': 'Civil',
    '05': 'Design',
    '06': 'BSBE',
    '07': 'CL',
    '08': 'EEE',
    '21': 'Physics',
    '22': 'Chemistry',
    '23': 'MNC',
    '41': 'HSS',
    '51': 'Energy',
    '52': 'Environment',
    '53': 'Nano-Tech',
    '54': 'Rural-Tech',
    '55': 'Linguistics',
	'61': 'Others',
	'62': 'Others',
	'63': 'Others',
}

def deptIdentify(rollNumber):
    roll = rollNumber
    program= None
    if roll[2]=='0':
        program='UG'
    else:
        program="PG"
    
    dept = deptList[roll[4:6]]

    return dept


def csv_to_voter():
	csvfile = open('voter.csv', 'r')
	reader = csv.reader(csvfile, quoting=csv.QUOTE_ALL)
	for i, row in enumerate(reader):
		print("voter", i+1)
		username = smart_str(row[0]).lower()
		category = smart_str(row[1])
		rollNumber = smart_str(row[2])
		dept = deptIdentify(smart_str(row[2]))  
		vote_string1=""
		vote_string2=""
		vote_time = ""
		voter_loc = Point(0.0,0.0)
		voter = Voter(username=username,
			category=category,
			rollNumber=int(rollNumber),
			dept=dept,
			vote_string1 = vote_string1,
			vote_string2 = vote_string2,
			vote_time= vote_time,
			voter_location = voter_loc
		)

		voter.save()

def csv_to_contestants():
	csvfile = open('contestant.csv', 'r')
	reader = csv.reader(csvfile, quoting=csv.QUOTE_ALL)
	for i, row in enumerate(reader):
		print("contestant ",i+1)
		contestant=Contestant(name=row[0],email = row[1], post = row[2], rollNumber = row[3], video=row[4], tagline = row[5],agenda1 = row[6], agenda2 = row[7], agenda3 = row[8], agenda4 = row[9], pic = "contestants/" + row[3]+".jpg", agendaPDF= "agenda/" + row[3]+".pdf", random_suppling = 0)
		contestant.save()

def run():
	Voter.objects.all().delete()
	# Contestant.objects.all().delete()
	csv_to_voter()
	# csv_to_contestants()	
