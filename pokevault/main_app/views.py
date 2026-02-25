from django.shortcuts import render, redirect
from .models import Card
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import ConditionForm

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

def card_detail(request, pk):
    card = Card.objects.get(id=pk)
    condition_form = ConditionForm()
    return render(request, 'cards/detail.html', {
        'card': card,
        'condition_form': condition_form,
    })

def add_condition(request, card_id):
    form = ConditionForm(request.POST)
    if form.is_valid():
        new_condition = form.save(commit=False)
        new_condition.card_id = card_id
        new_condition.save()
    return redirect('card-detail', pk=card_id)

class CardList(ListView):
    model = Card
    template_name = 'cards/index.html'

class CardCreate(CreateView):
    model = Card
    fields = ['name', 'set_name', 'rarity', 'description']

class CardUpdate(UpdateView):
    model = Card
    fields = ['name', 'set_name', 'rarity', 'description']

class CardDelete(DeleteView):
    model = Card
    success_url = '/cards'