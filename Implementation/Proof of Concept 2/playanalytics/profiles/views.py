from django.shortcuts import render, get_object_or_404, redirect
from .models import Player
from .forms import PlayerForm, JournalEntryForm

# Create your views here.

def player_list(request):
    players = Player.objects.all()
    return render(request, 'profiles/player_list.html', {'players': players})

def player_detail(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    entries = player.journal_entries.all()
    return render(request, 'profiles/player_detail.html', {'player': player, 'entries': entries})

def edit_player(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    form = PlayerForm(request.POST or None, request.FILES or None, instance=player)
    if form.is_valid():
        form.save()
        return redirect('profiles:player_detail', player.id)
    return render(request, 'profiles/edit_player.html', {'form': form, 'player': player})

def add_journal_entry(request, player_id):
    player = get_object_or_404(Player, id=player_id)
    form = JournalEntryForm(request.POST or None)
    if form.is_valid():
        entry = form.save(commit=False)
        entry.player = player
        entry.save()
        return redirect('profiles:player_detail', player.id)
    return render(request, 'profiles/journal_entry.html', {'form': form, 'player': player})
