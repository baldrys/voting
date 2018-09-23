from django.http import HttpResponseRedirect
from django.shortcuts import render
from voting_app.utils import *

# Create your views here.

def home(request):

    page_title = 'Главная'

    return render(request, 'home/index.html', locals())

def activeVotes(request):

    page_title = 'Активные голосования'
    votes_name = page_title
    listOfeVotes = active_votes()

    return render(request, 'votes/votes.html', locals())

def completedVotes(request):

    page_title = 'Завершенные голосования'
    votes_name = page_title
    listOfeVotes = completed_votes()

    return render(request, 'votes/votes.html', locals())

def detailVote(request, id):

    vote = Vote.objects.get(id=id)
    voteForChars = vote.voteforcharacter_set.all()
    page_title = vote.title
    votes_name = page_title

    if is_active_vote(vote):
        if request.method == "GET":
            nominates = voteForChars
            return render(request, 'voteDetail/activeVoteDetail.html', locals())
        if request.method == "POST":
            idToVote = request.POST.get("idToVote")
            charToVote = voteForChars.get(character__id=idToVote)
            charToVote.votes_number += 1
            charToVote.save()
            return HttpResponseRedirect('/')
    else:
        winners = []
        topFives = []
        sorted = vote.voteforcharacter_set.order_by('-votes_number')
        if sorted.count() !=0:
            winnerNumberVotes = sorted[0].votes_number
            winners = voteForChars.filter(votes_number__exact=winnerNumberVotes)
            topFives = sorted[winners.count():5]

        return render(request, 'voteDetail/completedVoteDetail.html', locals())