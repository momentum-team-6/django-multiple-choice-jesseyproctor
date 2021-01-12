from django.shortcuts import render
from .models import Deck, Card

# Create your views here.
def homepage(request):
    decks = Deck.objects.all().order_by('-date')
    context = {'decks': decks}
    return render(request, 'homepage.html', context)


def makeDeck(request):
    return render(request, )


def deleteDeck(request):
    return render(request, )


def editDeck(request):
    return render(request, )


def makeCard(request):
    return render(request, )


def deleteCard(request):
    return render(request, )


def editCard(request):
    return render(request, )


def showDeck(request):
    return render(request, )




