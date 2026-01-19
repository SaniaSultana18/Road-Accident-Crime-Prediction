import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os


# Page config
st.set_page_config(page_title="Road Accident & Crime Risk Analysis", layout="wide")
st.title("🚨 Road Accident & Crime Risk Analysis Dashboard")

st.markdown(
    "This dashboard analyzes road accident and crime data across Indian States/UTs to identify high-risk regions using a composite risk score."
)

# ----------------- Load Data -----------------
if not os.path.exists("outputs/final_risk_analysis.csv"):
    st.error("Required data file not found. Please run main.py first.")
    st.stop()

merged_df = pd.read_csv("outputs/final_risk_analysis.csv")

# ----------------- 1️⃣ Merged Data Preview -----------------
st.subheader("Merged Data Preview")
st.dataframe(merged_df)

# ----------------- 2️⃣ Key Metrics -----------------
st.subheader("Key Metrics")
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Total States/UTs", merged_df['State'].nunique())
col2.metric("Total Crime Cases", int(merged_df["Cases_Reported"].sum()))
col3.metric("Total Child Victims", int(merged_df["Child_Victims"].sum()))
col4.metric("Total Adult Victims", int(merged_df["Adult_Victims"].sum()))
col5.metric("Total Road Accident Cases", int(merged_df["Road_Accidents_Cases"].sum()))

st.metric("Total Deaths (Road Accidents)", int(merged_df["Road_Accidents_Died"].sum()))

# ----------------- 3️⃣ Crime Distribution Pie Chart -----------------
st.subheader("Crime Distribution: Child vs Adult Victims")
crime_values = [merged_df["Child_Victims"].sum(), merged_df["Adult_Victims"].sum()]
crime_labels = ["Child Victims", "Adult Victims"]

fig2, ax2 = plt.subplots()
ax2.pie(crime_values, labels=crime_labels, autopct='%1.1f%%', colors=['#ff9999','#66b3ff'])
ax2.set_title("Proportion of Child vs Adult Victims")
fig2.tight_layout()
st.pyplot(fig2)

# ----------------- 4️⃣ Risk Level Distribution -----------------
st.subheader("Risk Level Distribution")
risk_counts = merged_df['Risk_Level'].value_counts()
fig1, ax1 = plt.subplots()
ax1.bar(risk_counts.index, risk_counts.values, color=['red', 'green', 'orange'])
ax1.set_xlabel("Risk Level")
ax1.set_ylabel("Number of States")
ax1.set_title("Number of States by Risk Level")
fig1.tight_layout()
st.pyplot(fig1)

# ----------------- 5️⃣ Top 10 High Risk States -----------------
st.subheader("Top 10 High Risk States")
top10_high = merged_df.sort_values("Risk_Score", ascending=False).head(10)
st.bar_chart(top10_high.set_index("State")["Risk_Score"])

# ----------------- 6️⃣ Road Accidents: Cases vs Deaths -----------------
st.subheader("Road Accidents: Cases vs Deaths")
fig3, ax3 = plt.subplots(figsize=(10,5))
ax3.bar(merged_df['State'], merged_df['Road_Accidents_Cases'], label="Cases", color='#ffa500')
ax3.bar(merged_df['State'], merged_df['Road_Accidents_Died'], label="Deaths", color='#ff4500', bottom=merged_df['Road_Accidents_Cases'])
ax3.set_xticks(range(len(merged_df['State'])))
ax3.set_xticklabels(merged_df['State'], rotation=90)
ax3.set_ylabel("Number")
ax3.set_title("Road Accident Cases vs Deaths by State")
ax3.legend()
fig3.tight_layout()
st.pyplot(fig3)

# ----------------- 7️⃣ Check Risk Details by State -----------------
st.subheader("Check Risk Details by State / UT")
state_selected = st.selectbox("Select a State/UT", merged_df['State'].unique())
state_data = merged_df[merged_df['State'] == state_selected]
st.dataframe(state_data[[
    "State",
    "Cases_Reported",
    "Child_Victims",
    "Adult_Victims",
    "Total_Victims",
    "Road_Accidents_Cases",
    "Road_Accidents_Died",
    "Risk_Score",
    "Risk_Level"
]])



# ----------------- 8️⃣ Optional: Save Charts -----------------
if st.button("Save All Charts"):
    fig1.savefig("outputs/risk_level_distribution.png")
    fig2.savefig("outputs/crime_distribution.png")
    fig3.savefig("outputs/road_accidents.png")
    st.success("All charts saved in the outputs folder!")
