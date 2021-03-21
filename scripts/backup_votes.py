import csv
from voter.models import Voter

filename = 'backup_votes.csv'



def backup_votes(vote1,vote2,vote_time):
    backup_string=[vote1,vote2,vote_time]
    with open(filename, 'a+') as backup:
        backup_writer=csv.writer(backup)
        backup_writer.writerow(backup_string)
        
def backup():
    voters = Voter.objects.filter(final_submit=True)
    for id,voter in enumerate(voters):
        print('backing up ',id)
        backup_votes(voter.vote_string1,voter.vote_string2,voter.vote_time)

def run():
    backup()