import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import joblib
import numpy as np

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("player_data_enhanced.csv")
    return df

df = load_data()

st.title("Player Injury Risk Analysis and Prediction")

# Sidebar filters for interaction
st.sidebar.header("Filter by Player Attributes")
selected_position = st.sidebar.selectbox("Select Position", options=df["Position"].unique())
selected_age = st.sidebar.slider("Select Age Range", int(df["Age"].min()), int(df["Age"].max()), (20, 35))

filtered_df = df[(df["Position"] == selected_position) & 
                 (df["Age"] >= selected_age[0]) & (df["Age"] <= selected_age[1])]

# KPI Metrics
st.subheader("Player Overview")
st.metric("Total Players", len(filtered_df))
st.metric("Average Age", round(filtered_df["Age"].mean(), 1))
st.metric("Average Total Injuries", round(filtered_df["Total_Injuries"].mean(), 1))

# Pie Chart: % of Injuries by Type
st.subheader("% of Injuries by Type")
injury_columns = [col for col in df.columns if 'Number_of_' in col and '_Injuries' in col]
injury_sums = df[injury_columns].sum().sort_values(ascending=False).head(5)
fig1, ax1 = plt.subplots()
ax1.pie(injury_sums, labels=injury_sums.index.str.replace('Number_of_', '').str.replace('_Injuries', ''), 
        autopct='%1.1f%%', startangle=90, colors=plt.cm.tab20.colors)
ax1.axis('equal')
st.pyplot(fig1)

# Bar Chart: Average Total Injuries per Position
st.subheader("Average Total Injuries per Position")
avg_injuries = df.groupby("Position")["Total_Injuries"].mean().sort_values(ascending=False).reset_index()
fig2, ax2 = plt.subplots()
ax2.bar(avg_injuries["Position"], avg_injuries["Total_Injuries"], color='tomato')
ax2.set_ylabel("Average Total Injuries")
ax2.set_title("Avg Injuries by Position")
st.pyplot(fig2)

# Stacked Bar Chart: Risk Level Distribution by Position
st.subheader("Risk Level Distribution per Position")
risk_dist = pd.crosstab(df["Position"], df["Risk_Level"])
fig3, ax3 = plt.subplots()
risk_dist.plot(kind='bar', stacked=True, ax=ax3, colormap='plasma')
ax3.set_ylabel("Number of Players")
ax3.set_title("Risk Level by Position")
st.pyplot(fig3)

# Data Summary Table
st.subheader("Filtered Player Data")
st.dataframe(filtered_df)

# Injury Risk Prediction Input Form
st.sidebar.header("Predict Injury Risk")
name = st.sidebar.text_input("Player Name")
position = st.sidebar.selectbox("Prediction - Position", df["Position"].unique())
height = st.sidebar.number_input("Height (inches)", min_value=60, max_value=90)
weight = st.sidebar.number_input("Weight (pounds)", min_value=120, max_value=350)
age = st.sidebar.number_input("Age", min_value=18, max_value=45)
avg_minutes = st.sidebar.number_input("Avg Minutes Per Game", min_value=0.0, max_value=48.0)
avg_fg_attempts = st.sidebar.number_input("Avg Field Goals Attempted", min_value=0.0)
steals = st.sidebar.number_input("Steals Per Game", min_value=0.0)
blocks = st.sidebar.number_input("Blocks Per Game", min_value=0.0)
fouls = st.sidebar.number_input("Fouls Per Game", min_value=0.0)
total_injuries = st.sidebar.number_input("Total Injuries", min_value=0)
cumulative_load = avg_minutes * 82  # Assuming 82 games per season

# Predict Button
if st.sidebar.button("Predict Injury Risk"):
    try:
        model = joblib.load("rf_injury_model.joblib")
        input_features = np.array([[
            avg_minutes, avg_fg_attempts, steals, blocks, fouls,
            cumulative_load, age, height, weight, total_injuries
        ]])
        prediction = model.predict(input_features)
        risk_levels = ['Low', 'Low-Medium', 'Medium', 'Medium-High', 'High']
        predicted_risk = risk_levels[int(prediction[0])]

        st.sidebar.success(f"Predicted Injury Risk Level: {predicted_risk}")

        # Display predicted player as a table/chart below main area
        st.subheader(f"Prediction Summary for {name if name else 'Player'}")
        summary_data = pd.DataFrame([{
            "Name": name,
            "Position": position,
            "Age": age,
            "Height": height,
            "Weight": weight,
            "Avg Minutes": avg_minutes,
            "Avg FG Attempts": avg_fg_attempts,
            "Total Injuries": total_injuries,
            "Predicted Risk": predicted_risk
        }])
        st.dataframe(summary_data)

    except Exception as e:
        st.sidebar.error("Model could not be loaded or prediction failed.")
        st.sidebar.error(str(e))
