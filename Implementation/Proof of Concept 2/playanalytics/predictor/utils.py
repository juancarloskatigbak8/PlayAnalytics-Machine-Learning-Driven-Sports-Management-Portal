import joblib
import numpy as np

def predict_risk_level(player):
    model = joblib.load('rf_injury_model.joblib')
    features = np.array([[
        player.avg_minutes, player.avg_fg_attempts, player.steals,
        player.blocks, player.fouls, player.avg_minutes * 82,
        player.age, player.height, player.weight, player.total_injuries
    ]])
    prediction = model.predict(features)
    labels = ['Low', 'Low-Medium', 'Medium', 'Medium-High', 'High']
    return labels[int(prediction[0])]
