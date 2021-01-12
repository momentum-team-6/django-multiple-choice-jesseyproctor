from django.shortcuts import render, redirect, get_object_or_404
from .models import Deck, Card
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import DeckForm, CardForm
from django.urls import reverse

# Create your views here.
def homepage(request):
    decks = Deck.objects.all().order_by('-date')
    #stored context in a variable to remind myself what's happening
    context = {'decks': decks}
    return render(request, 'homepage.html', context)

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #save user
            user = form.save()
            #log user in
            login(request, user)
            return redirect('login_view') #where should I redirect, lookup to = 
    else:
        form = UserCreationForm()
    return render(request, 'signup_view.html', {'form':form})


def login_view(request):
    if request.method =='POST':
        #have to name request.POST because it's not naturally the first expected perameter of the authentification form function
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #log in user 
            user = form.get_user()
            login(request,user)
            return redirect('homepage') #where should I redirect
            #add create deck link on homepage or redirect to create deck
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

def logout_view(request):
    if request.method =='POST':
        logout(request)
        return redirect('homepage')

def make_deck(request):
    if request.method == 'POST':
        form = DeckForm(request.POST)
        # check if form is valid
        if form.is_valid():
            #save the form
            new_deck = form.save()
            return redirect('make_card', pk=new_deck.pk )
            
    else:
        form = DeckForm()
    return render(request, 'make_edit_deck.html', {'form': form} )


def delete_deck(request):
    pass


def edit_deck(request):
    pass


def make_card(request, pk):
    deck_obj = get_object_or_404(Deck, pk=pk)
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('view_deck', deck_obj.pk)) 
    else:
        #The initial argument lets you specify the initial value to use when rendering this Field in an unbound Form
        form = CardForm(initial={'parentDeck':deck_obj})
    return render(request, 'make_edit_card.html', {'form': form})


def delete_card(request):
    pass


def edit_card(request):
    pass


def view_deck(request, pk):
    # deck_obj = get_object_or_404(Deck, pk)
    # card_list = deck_obj.card_set.all()
    # card_obj = card_list.first()
    # if request.method == 'GET' and 'card' in request.GET:
    #     card_obj = get_object_or_404(Card, pk=request.GET['card'])
    # context = {'deck_obj': deck_obj, 'card_obj':card_obj}
    # return render(request, 'flashcards/viewDeck.html', context)
    pass




