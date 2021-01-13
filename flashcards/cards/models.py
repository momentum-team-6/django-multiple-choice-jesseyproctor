from django.db import models
from datetime import datetime


# Create your models here.
class Card(models.Model):
    parentDeck = models.ForeignKey('Deck', on_delete=models.CASCADE) #Deck in quotes because Deck model read after this one. #on delete, cascade means delete all children of parents when you delete parent
    front = models.TextField()
    back = models.TextField()

    def __str__(self):
        return self.front

    def has_prev_card(self):
    #True if the current card isn't the first card in your deck
        first_card_in_deck = self.parentDeck.card_set.first()
        if self == first_card_in_deck:
            return False
        return True

    def get_prev_card(self):
    #to get last card you looked at
        return self.parentDeck.card_set.filter(id__lt=self.id).last()


    def has_next_card(self):
    #True if current card isnt the last one in your deck
        last_card_in_deck = self.parentDeck.card_set.last()
        if self == last_card_in_deck:
            return False
        return True

    def get_next_card(self):
    #Gives you the next card in your deck
        return self.parentDeck.card_set.filter(id__gt=self.id).first()



class Deck(models.Model): 
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=1000, null=False, blank=True) #User can leave blank
    date = models.DateTimeField(default=datetime.now, blank=True) #add date for ordering purposes
    

    def __str__(self):
        return self.title



