import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

# Load enhanced dataset
df = pd.read_csv("player_data_enhanced.csv")

# Select features and target
features = [
    "Minutes_per_game", "FG_Attempts_per_game", "Steals_per_game", "Blocks_per_game",
    "Fouls_per_game", "Cumulative_Load", "Age", "Height_in_Inches", "Weight_in_Pounds", "Total_Injuries"
]

df = df.dropna(subset=features + ["Risk_Level"])
X = df[features]
le = LabelEncoder()
y = le.fit_transform(df["Risk_Level"])

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, test_size=0.2, random_state=42)

# Train model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Save model
joblib.dump(rf_model, "rf_injury_model.joblib")
print("✅ Model retrained and saved as rf_injury_model.joblib")
