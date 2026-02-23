from django.shortcuts import render
from .models import Card

# class Card:
#     def __init__(self, name, set_name, rarity, description):
#         self.name = name
#         self.set_name = set_name
#         self.rarity = rarity
#         self.description = description

# # Create a list of Card instances
# cards = [
#     Card('Charizard', 'Base Set', 'Rare Holo', 'A powerful fire type Pokemon card.'),
#     Card('Pikachu', 'Jungle', 'Common', 'The most iconic Pokemon card.'),
#     Card('Mewtwo', 'Base Set', 'Rare Holo', 'A psychic powerhouse.'),
#     Card('Blastoise', 'Base Set', 'Rare Holo', 'A water type fan favourite.'),
# ]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def card_index(request):
    cards = Card.objects.all()
    return render(request, 'cards/index.html', {'cards': cards})