import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
