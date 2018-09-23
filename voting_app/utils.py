from voting_app.models import *
from django.utils import timezone

def is_active_vote(vote):
    if vote.end_date < timezone.now() or timezone.now() < vote.start_date :
        return False

    # listOfWinners =  vote.voteforcharacter_set.filter(votes_number__gte=vote.votes_to_win)
    # if listOfWinners.count() != 0:
    #     # print("Есть победители")
    #     return False

    if vote.voteforcharacter_set.latest('votes_number').votes_number >= vote.votes_to_win:
        return False

    return True

def is_completed_vote(vote):
    return not (is_active_vote(vote)) and timezone.now() > vote.start_date

def active_votes():
    listOfActiveVotes = []

    for vote in Vote.objects.all():
        if is_active_vote(vote):
            listOfActiveVotes.append(vote)
    return listOfActiveVotes

def completed_votes():
    listOfCompletedVotes = []

    for vote in Vote.objects.all():
        if is_completed_vote(vote):
            listOfCompletedVotes.append(vote)
    return listOfCompletedVotes

# def votes(vote_type):
#
#     listOfVotes = []
#     for vote in Vote.objects.all():
#         if vote_type == 'ACTIVE':
#
#         if is_active_vote(vote):
#             listOfActiveVotes.append(vote)
#     return listOfActiveVotes
