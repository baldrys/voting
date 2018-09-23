from voting_app.models import *
from django.utils import timezone

def is_active_vote(vote):
    if vote.end_date < timezone.now() or timezone.now() < vote.start_date :
        return False
    if vote.vote_for_character_set.latest('votes_number').votes_number >= vote.votes_to_win:
        return False
    return True

def is_completed_vote(vote):
    return not (is_active_vote(vote)) and timezone.now() > vote.start_date

def active_votes():
    list_of_active_votes = []
    for vote in Vote.objects.all():
        if is_active_vote(vote):
            list_of_active_votes.append(vote)
    return list_of_active_votes

def completed_votes():
    list_of_completed_votes = []
    for vote in Vote.objects.all():
        if is_completed_vote(vote):
            list_of_completed_votes.append(vote)
    return list_of_completed_votes
