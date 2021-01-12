from django.shortcuts import render, redirect
from .models import Deck, Card
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def homepage(request):
    decks = Deck.objects.all().order_by('-date')
    context = {'decks': decks}
    return render(request, 'homepage.html', context)

def register_user(request):
    if request.method == 'POST':
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            #log user in
            return redirect(homepage.html) #where should I redirect
    else:
        signup_form = UserCreationForm()
    return render(request, 'register_user.html', {'signup_form':signup_form})


def login(request):
    if request.method =='POST':
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            #log in user
            return redirect(homepage.html) #where should I redirect
    else:
        login_form = AuthenticationForm()
    return render(request, 'login.html', {'login_form':login_form})

def make_deck(request):
    pass


def delete_deck(request):
    pass


def edit_deck(request):
    pass


def make_card(request):
    pass


def delete_card(request):
    pass


def edit_card(request):
    pass


def view_deck(request):
    pass




