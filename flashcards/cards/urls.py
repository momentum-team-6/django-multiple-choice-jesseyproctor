from django.urls import path
from .import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('decks/make/', views.make_deck, name='make_deck'),
    path('decks/edit/', views.edit_deck, name='edit_deck'),
    path('decks/delete/', views.delete_deck, name='delete_deck'),
    path('cards/make/', views.make_card, name='make_card'),
    path('cards/edit/', views.edit_card, name='edit_card'),
    path('cards/delete/', views.delete_card, name='delete_card'),
    path('decks/view/', views.view_deck, name='view_deck'),
    path('signup/', views.register_user, name='register_user'),
    path('login/', views.login, name='login'),
]
