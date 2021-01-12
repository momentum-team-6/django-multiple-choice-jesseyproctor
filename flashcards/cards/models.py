from django.db import models


# Create your models here.
class Card(models.Model):
    parentDeck = models.ForeignKey('Deck', on_delete=models.CASCADE) #Deck in quotes because Deck model read after this one.
    front = models.TextField()
    back = models.TextField()

    def __str__(self):
        return self.front


class Deck(models.Model): 
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=1000, null=False, blank=True) #User can leave blank
    datetime = models.DateTimeField(auto_now_add=True) #add date for ordering purposes
    

    def __str__(self):
        return self.title


