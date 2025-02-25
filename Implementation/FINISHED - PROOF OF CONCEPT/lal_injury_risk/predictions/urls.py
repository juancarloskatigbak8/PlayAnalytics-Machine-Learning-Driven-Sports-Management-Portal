from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.shortcuts import redirect
from .views import home, player_predictions, add_player, register
from .models import Player
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import io
import urllib, base64

@login_required
def player_predictions(request):
    """
    View to display dynamically calculated injury risk predictions with a density plot.
    """
    players = Player.objects.filter(user=request.user)
    
    # Prepare data for visualization
    risk_levels = [player.calculate_risk() for player in players]
    risk_map = {"Low": 1, "Medium": 2, "High": 3}  # Convert categories to numeric values
    risk_numeric = [risk_map[risk] for risk in risk_levels]
    
    # Create the density plot
    plt.figure(figsize=(8,5))
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

def logout_view(request):
    logout(request)
    return redirect('login') 

urlpatterns = [
    path("", home, name="home"),
    path('register/', register, name='register'),
    path("predictions/", player_predictions, name="player_predictions"),
    path("add_player/", add_player, name="add_player"),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
