import csv

filename = 'backup_votes.csv'



def backup_votes(vote1,vote2,vote_time):
    backup_string=[vote1,vote2,vote_time]
    with open(filename, 'a+') as backup:
        backup_writer=csv.writer(backup)
        backup_writer.writerow(backup_string)
        
    