import pandas as pd
from django.shortcuts import render
from profiles.models import Player

# Create your views here.

def dashboard_view(request):
    players = Player.objects.all()
    total_players = players.count()
    avg_age = round(players.aggregate(pd.NamedAgg(column='age', aggfunc='mean'))['age'], 1) if total_players else 0
    avg_injuries = round(players.aggregate(pd.NamedAgg(column='total_injuries', aggfunc='mean'))['total_injuries'], 1) if total_players else 0

    # Pie data (most common injuries - placeholder data or derived logic)
    pie_labels = ['Ankle', 'Knee', 'Back', 'Quad', 'Hamstring']
    pie_values = [24, 18, 12, 9, 7]

    # Bar chart (avg injuries per position)
    df = pd.DataFrame(list(players.values('position', 'total_injuries')))
    bar_data = df.groupby('position')['total_injuries'].mean().sort_values(ascending=False)
    bar_labels = list(bar_data.index)
    bar_values = list(bar_data.values)

    context = {
        'total_players': total_players,
        'avg_age': avg_age,
        'avg_injuries': avg_injuries,
        'pie_labels': pie_labels,
        'pie_values': pie_values,
        'bar_labels': bar_labels,
        'bar_values': bar_values,
    }

    return render(request, 'dashboard/dashboard.html', context)