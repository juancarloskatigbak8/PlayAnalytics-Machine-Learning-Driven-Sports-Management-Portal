from django.shortcuts import render, redirect
from profiles.forms import PlayerForm
from .utils import predict_risk_level

# Create your views here.

def predict_player(request):
    form = PlayerForm(request.POST or None, request.FILES or None)
    prediction = None

    if request.method == 'POST' and form.is_valid():
        player = form.save(commit=False)
        prediction = predict_risk_level(player)
        player.predicted_risk = prediction
        player.save()
        return redirect('profiles:player_detail', player.id)

    return render(request, 'predictor/predict.html', {'form': form, 'prediction': prediction})
