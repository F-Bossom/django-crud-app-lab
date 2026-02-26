from django.shortcuts import render, redirect
from .models import Card, Tag
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import ConditionForm, CardForm
from django.urls import reverse

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
    tags = Tag.objects.exclude(id__in = card.tags.all().values_list('id'))
    return render(request, 'cards/detail.html', {
        'card': card,
        'condition_form': condition_form,
        'tags': tags,
    })

def add_condition(request, card_id):
    form = ConditionForm(request.POST)
    if form.is_valid():
        new_condition = form.save(commit=False)
        new_condition.card_id = card_id
        new_condition.save()
    return redirect('card-detail', pk=card_id)

def associate_tag(request, card_id, tag_id):
    Card.objects.get(id=card_id).tags.add(tag_id)
    return redirect('card-detail', pk=card_id)

class CardList(ListView):
    model = Card
    template_name = 'cards/index.html'

class CardCreate(CreateView):
    model = Card
    form_class = CardForm

class CardUpdate(UpdateView):
    model = Card
    form_class = CardForm

class CardDelete(DeleteView):
    model = Card
    success_url = '/cards'

class TagCreate(CreateView):
    model = Tag
    fields = '__all__'

class TagDetail(DetailView):
    model = Tag
    template_name = 'tags/detail.html'

class TagList(ListView):
    model = Tag
    template_name = 'tags/index.html'

class TagUpdate(UpdateView):
    model = Tag
    fields = ['name']

class TagDelete(DeleteView):
    model = Tag
    success_url = '/tags/'