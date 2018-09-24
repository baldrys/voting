from django.http import HttpResponseRedirect
from django.shortcuts import render
from voting_app.utils import *

# Create your views here.

def home(request):
    page_title = 'Главная'
    return render(request, 'home/index.html', locals())

def active_votes_view(request):
    page_title = 'Активные голосования'
    votes_name = page_title
    # listOfeVotes = active_votes()
    list_of_votes = get_list_of_votes("active")
    return render(request, 'votes/votes.html', locals())

def completed_votes_view(request):
    page_title = 'Завершенные голосования'
    votes_name = page_title
    # listOfeVotes = completed_votes()
    list_of_votes = get_list_of_votes("completed")
    return render(request, 'votes/votes.html', locals())

def detail_vote_view(request, id):
    vote = Vote.objects.get(id=id)
    vote_for_chars = vote.vote_for_character_set.all()
    page_title = vote.title
    votes_name = page_title
    if is_active_vote(vote):
        if request.method == "GET":
            nominates = vote_for_chars
            return render(request, 'voteDetail/activeVoteDetail.html', locals())
        if request.method == "POST":
            id_to_vote = request.POST.get("id_to_vote")
            charToVote = vote_for_chars.get(character__id=id_to_vote)
            charToVote.votes_number += 1
            charToVote.save()
            return HttpResponseRedirect('/')
    else:
        winners = []
        topFives = []
        if vote.vote_for_character_set.count() != 0:
            sorted = vote.vote_for_character_set.order_by('-votes_number')
            winner_number_votes = sorted[0].votes_number
            winners = vote_for_chars.filter(votes_number__exact=winner_number_votes)
            topFives = sorted[winners.count():5 + winners.count()]
        return render(request, 'voteDetail/completedVoteDetail.html', locals())