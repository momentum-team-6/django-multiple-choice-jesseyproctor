from django.shortcuts import render, redirect, get_object_or_404
from .models import Deck, Card
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .forms import DeckForm, CardForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required

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

#need template for logout
def logout_view(request):
    if request.method == 'GET':
        logout(request)
    return redirect('homepage')
    

@login_required(login_url='login/')
def make_deck(request):
    #GET renders the form, POST adds form info to database
    #decks are not currently associated with a specific user. 
    if request.method == 'GET':
        form = DeckForm()
    if request.method == 'POST':
        form = DeckForm(request.POST)
        # check if form is valid
        if form.is_valid():
            #save the form
            new_deck = form.save()
            return redirect('make_card', deck_pk=new_deck.pk )
                    
    return render(request, 'make_edit_deck.html', {'form': form} )


def delete_deck(request, deck_pk):
    deck_obj = get_object_or_404(Deck, pk=deck_pk)
    deck_obj.delete()
    return redirect('homepage')


def edit_deck(request, deck_pk):
    deck_obj = get_object_or_404(Deck, pk=deck_pk)
    if request.method == 'POST':
        # pulls the form
        form = DeckForm(request.POST, instance=deck_obj)
        if form.is_valid():
            form.save()
            return redirect(to='view_deck', deck_pk=deck_obj.pk)
    else:
        form = DeckForm(instance=deck_obj)
    context = {'form': form, 'edit_mode':True, 'deck_obj':deck_obj}
    return render(request, 'make_edit_deck.html', context)

@login_required(login_url='login/')
def make_card(request, deck_pk):
    # #write out as simply as possible:
    # if request.method == 'GET':
    #     form = CardForm()
    # if request.method == 'POST':
    #     form = CardForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('view_deck', pk)

    deck_obj = get_object_or_404(Deck, pk=deck_pk)
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            new_card = form.save(commit=False) #store new card in a variable, youre not ready to save it to database
            new_card.parentDeck=deck_obj #new card with the parent deck from database equals your deck object
            new_card.save() #now you're ready to save it
            return redirect('view_deck', deck_pk=deck_obj.pk)
    else:
        form = CardForm()
    return render(request, 'make_edit_card.html', {'form': form})
        

def delete_card(request, card_pk):
    card_obj = get_object_or_404(Card, pk=card_pk)
    card_obj.delete()
    return redirect(to='view_deck', deck_pk=card_obj.parentDeck.pk)


def edit_card(request, card_pk):
    #the instance allows it to grab a particular card to edit
    card_obj = get_object_or_404(Card, pk=card_pk)
    if request.method == 'POST':
        form = CardForm(request.POST, instance=card_obj)
        if form.is_valid():
            form.save()
            return redirect(to='view_deck', deck_pk=card_obj.parentDeck.pk)
    else:
        form = CardForm(instance=card_obj)
    context = {'form':form, 'edit_mode':True, 'card_obj':card_obj}
    return render(request, 'make_edit_card.html', context)


def view_deck(request, deck_pk):
    # Grabs deck from database, Returns first card in deck 
    deck_obj = get_object_or_404(Deck, pk=deck_pk)
    card_list = deck_obj.card_set.all() #all cards from set
    card_obj = card_list.first() #first card in deck
    if request.method == 'GET' and 'card' in request.GET: #look up how to add condition for card being in parent deck
        card_obj = get_object_or_404(Card, pk=request.GET['card'])
    context = {'deck_obj': deck_obj, 'card_obj':card_obj}
    return render(request, 'view_deck.html', context)




