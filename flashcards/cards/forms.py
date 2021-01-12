from django.forms import ModelForm
from .models import Card, Deck

class DeckForm(ModelForm):
    class Meta:
        model = Deck
        fields = ['title', 'description']
        #may need a date input.  Come back to this

class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ['parentDeck', 'front', 'back']