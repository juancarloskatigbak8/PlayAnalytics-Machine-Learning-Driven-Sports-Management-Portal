from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Player
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import io
import urllib, base64
from .forms import PlayerForm

@login_required
def add_player(request):
    """
    View to allow authenticated users to add new players.
    """
    if request.method == "POST":
        form = PlayerForm(request.POST)
        if form.is_valid():
            player = form.save(commit=False)
            player.user = request.user  # Assign current user to the player
            player.save()
            return redirect('player_predictions')  # Redirect to predictions page
    else:
        form = PlayerForm()
    
    return render(request, 'predictions/add_player.html', {'form': form})

@login_required
def player_predictions(request):
    """
    View to display dynamically calculated injury risk predictions with a density plot.
    """
    players = Player.objects.filter(user=request.user)
    

    # Prepare data for visualization
    risk_levels = [player.calculate_risk() for player in players]
    risk_map = {"Low": 1, "Medium": 2, "High": 3}  # Convert categories to numeric values
    risk_numeric = [risk_map[risk] for risk in risk_levels] if risk_levels else [0]

    # Create the density plot
    plt.figure(figsize=(8, 5))
    sns.kdeplot(risk_numeric, fill=True, bw_adjust=0.5)
    plt.xticks([1, 2, 3], ["Low", "Medium", "High"])
    plt.xlabel("Injury Risk Level")
    plt.ylabel("Density")
    plt.title("Player Injury Risk Distribution")

    # Convert plot to a URL for embedding
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()
    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')

    context = {'players': players, 'graphic': graphic}
    return render(request, 'predictions/player_predictions.html', context)

def home(request):
    """
    View to display the home page.
    """
    return render(request, 'home.html')

def register(request):
    """
    View to handle user registration.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
