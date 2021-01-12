from django.urls import path
from .import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('decks/make/', views.makeDeck, name='make_deck'),
    path('decks/edit/', views.editDeck, name='edit_deck'),
    path('decks/delete/', views.deleteDeck, name='delete_deck'),
    path('cards/make/', views.makeCard, name='make_card'),
    path('cards/edit/', views.editCard, name='edit_card'),
    path('cards/delete/', views.deleteCard, name='delete_card'),
    path('decks/show/', views.showDeck, name='show_deck'),
]
