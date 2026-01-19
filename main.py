
# import pandas as pd
# import os

# # ----------------- Load Datasets -----------------
# crime_path = "data/crime_data/crime_2022.csv"      # update path if needed
# accident_path = "data/road_accident_2022.csv"

# crime_df = pd.read_csv(crime_path)
# accident_df = pd.read_csv(accident_path)

# print("Crime Dataset Info:")
# print(crime_df.info())
# print("\nRoad Accident Dataset Info:")
# print(accident_df.info())

# # ----------------- Clean Crime Data -----------------
# # Keep all relevant columns (for girls/child + adult victims)
# crime_cleaned = crime_df.copy()

# # Standardize State column name
# crime_cleaned.rename(columns={'State/UT (Col.3)': 'State'}, inplace=True)

# # ----------------- Clean Accident Data -----------------
# accident_cleaned = accident_df[['State/UT/City', 'Road Accidents - Cases', 'Road Accidents - Died']]
# accident_cleaned.rename(columns={'State/UT/City': 'State'}, inplace=True)

# # ----------------- Merge Datasets -----------------
# merged_full = pd.merge(crime_cleaned, accident_cleaned, on='State', how='inner')

# print("\nMerged Dataset Preview:")
# print(merged_full.head())

# # ----------------- Compute Risk Score -----------------
# # Normalize total victims and road accidents
# merged_full['Crime_Score'] = merged_full['Total Victims (Col.15) = (Col.9+ Col.14)'] / merged_full['Total Victims (Col.15) = (Col.9+ Col.14)'].max()
# merged_full['Accident_Score'] = merged_full['Road Accidents - Cases'] / merged_full['Road Accidents - Cases'].max()

# # Final risk score = average of crime + accident scores
# merged_full['Risk_Score'] = (merged_full['Crime_Score'] + merged_full['Accident_Score']) / 2

# # ----------------- Assign Risk Levels -----------------
# def classify_risk(score):
#     if score <= 0.33:
#         return "Low Risk"
#     elif score <= 0.66:
#         return "Medium Risk"
#     else:
#         return "High Risk"

# merged_full['Risk_Level'] = merged_full['Risk_Score'].apply(classify_risk)

# # ----------------- Save Full CSV -----------------
# os.makedirs("outputs", exist_ok=True)
# merged_full.to_csv("outputs/final_risk_analysis_full.csv", index=False)
# print("\nFull CSV with crime + accident + risk saved successfully!")

# # ----------------- Print Summary -----------------
# print("\nFinal Risk Classification:")
# print(merged_full[['State', 'Risk_Score', 'Risk_Level']])

# -----------------------------
# main.py
# ----------------
# 
#-------------
#===================================================================
# import pandas as pd
# import os

# # -----------------------------
# # Create outputs folder if not exists
# # -----------------------------
# if not os.path.exists("outputs"):
#     os.makedirs("outputs")

# # -----------------------------
# # Load datasets
# # -----------------------------
# crime_df = pd.read_csv("data/crime_datasets/crime_dataset.csv")
# acc_df = pd.read_csv("data/ADSI_Table_1A.2/road_accidents_2022.csv")

# # -----------------------------
# # Preview
# # -----------------------------
# print("Crime Dataset Info:")
# print(crime_df.info())
# print("\nRoad Accident Dataset Info:")
# print(acc_df.info())

# # -----------------------------
# # Clean Crime Data
# # -----------------------------
# # Keep relevant columns
# crime_cols = ["State/UT (Col.3)", "Cases Reported (Col.4)"] + crime_df.columns[4:15].tolist()
# clean_crime_df = crime_df[crime_cols].copy()
# clean_crime_df.rename(columns={"State/UT (Col.3)": "State"}, inplace=True)

# print("\nCleaned Crime Data:")
# print(clean_crime_df.head())

# # -----------------------------
# # Clean Accident Data
# # -----------------------------
# acc_df = acc_df[["State/UT/City", "Road Accidents - Cases", "Road Accidents - Died"]].copy()
# acc_df.rename(columns={"State/UT/City": "State"}, inplace=True)

# print("\nCleaned Accident Data:")
# print(acc_df.head())

# # -----------------------------
# # Merge datasets
# # -----------------------------
# merged_df = pd.merge(clean_crime_df, acc_df, on="State", how="inner")
# print("\nMerged Dataset (Crime + Accident):")
# print(merged_df.head())

# # -----------------------------
# # Calculate Risk Score
# # -----------------------------
# # Example formula (you can tweak weights)
# merged_df["Risk_Score"] = (
#     (merged_df["Total Victims (Col.15) = (Col.9+ Col.14)"] / merged_df["Total Victims (Col.15) = (Col.9+ Col.14)"].max()) * 0.5
#     + (merged_df["Road Accidents - Died"] / merged_df["Road Accidents - Died"].max()) * 0.5
# )

# # -----------------------------
# # Dynamic Risk Levels
# # -----------------------------
# low = merged_df["Risk_Score"].quantile(0.33)
# high = merged_df["Risk_Score"].quantile(0.66)

# def classify_risk_dynamic(score):
#     if score <= low:
#         return "Low Risk"
#     elif score <= high:
#         return "Medium Risk"
#     else:
#         return "High Risk"

# merged_df["Risk_Level"] = merged_df["Risk_Score"].apply(classify_risk_dynamic)

# # -----------------------------
# # Save Outputs
# # -----------------------------
# # Full dataset with all crime details
# merged_df.to_csv("outputs/final_risk_analysis_full.csv", index=False)

# # Summary CSV (optional)
# summary_cols = ["State", "Cases Reported (Col.4)", "Total Victims (Col.15) = (Col.9+ Col.14)",
#                 "Road Accidents - Cases", "Road Accidents - Died", "Risk_Score", "Risk_Level"]
# merged_df[summary_cols].to_csv("outputs/final_risk_analysis.csv", index=False)

# print("\nFinal Risk Classification:")
# print(merged_df[["State", "Risk_Score", "Risk_Level"]])
# print("\nFinal results saved to 'outputs/' folder.")
#=====================================================================================

# import pandas as pd
# import os

# # Create outputs folder if not exists
# if not os.path.exists("outputs"):
#     os.makedirs("outputs")

# # Load datasets
# crime_df = pd.read_csv("crime_data.csv")
# accident_df = pd.read_csv("road_accident_data.csv")

# # Clean crime dataset
# crime_clean = crime_df[["State/UT (Col.3)",
#                         "Cases Reported (Col.4)",
#                         "Victims of (Section 4 & 6 of POCSO Act r/w Section 376 IPC)Total Girl /Child Victims (Col.9)",
#                         "Victims of (Section 376 IPC)Total Women / Adult Victims (Col.14)",
#                         "Total Victims (Col.15) = (Col.9+ Col.14)"]].copy()
# crime_clean.rename(columns={
#     "State/UT (Col.3)": "State",
#     "Cases Reported (Col.4)": "Cases_Reported",
#     "Victims of (Section 4 & 6 of POCSO Act r/w Section 376 IPC)Total Girl /Child Victims (Col.9)": "Child_Victims",
#     "Victims of (Section 376 IPC)Total Women / Adult Victims (Col.14)": "Adult_Victims",
#     "Total Victims (Col.15) = (Col.9+ Col.14)": "Total_Victims"
# }, inplace=True)

# # Clean accident dataset
# accident_clean = accident_df[["State/UT/City",
#                               "Road Accidents - Cases",
#                               "Road Accidents - Died"]].copy()
# accident_clean.rename(columns={"State/UT/City": "State"}, inplace=True)

# # Merge datasets
# merged_df = pd.merge(crime_clean, accident_clean, on="State", how="inner")

# # Compute Risk Score (example formula)
# merged_df["Risk_Score"] = (
#     merged_df["Total_Victims"]/merged_df["Total_Victims"].max() * 0.5 +
#     merged_df["Road Accidents - Died"]/merged_df["Road Accidents - Died"].max() * 0.5
# )

# # Dynamic Risk Levels
# low = merged_df["Risk_Score"].quantile(0.33)
# high = merged_df["Risk_Score"].quantile(0.66)

# def classify_risk(score):
#     if score <= low:
#         return "Low Risk"
#     elif score <= high:
#         return "Medium Risk"
#     else:
#         return "High Risk"

# merged_df["Risk_Level"] = merged_df["Risk_Score"].apply(classify_risk)

# # Save full dataset for Streamlit
# merged_df.to_csv("outputs/final_risk_analysis_full.csv", index=False)
# print("Final result saved to outputs/final_risk_analysis_full.csv")






# ----------------- IMPORT LIBRARIES -----------------
import pandas as pd
import os

# File paths
crime_file = "data/crime_data.csv"
accident_file = "data/road_accidents_2022.csv"

# Load datasets
crime_df = pd.read_csv(crime_file, encoding="latin1")
accident_df = pd.read_csv(accident_file)

print("Crime data loaded:", crime_df.shape)
print("Accident data loaded:", accident_df.shape)


# ----------------- CLEAN CRIME DATA -----------------
crime_df_clean = crime_df[["State/UT (Col.3)", 
                           "Cases Reported (Col.4)",
                           "Victims of (Section 4 & 6 of POCSO Act r/w Section 376 IPC)Total Girl /Child Victims (Col.9)",
                           "Victims of (Section 376 IPC)Total Women / Adult Victims (Col.14)",
                           "Total Victims (Col.15) = (Col.9+ Col.14)"]].copy()

crime_df_clean.columns = ["State", "Cases_Reported", "Child_Victims", "Adult_Victims", "Total_Victims"]

# ----------------- CLEAN ACCIDENT DATA -----------------
accident_df_clean = accident_df[["State/UT/City", "Road Accidents - Cases", "Road Accidents - Died"]].copy()
accident_df_clean.columns = ["State", "Road_Accidents_Cases", "Road_Accidents_Died"]

# ----------------- MERGE DATA -----------------
merged_df = pd.merge(crime_df_clean, accident_df_clean, on="State", how="inner")

# ----------------- CALCULATE RISK SCORE -----------------
merged_df["Risk_Score"] = (merged_df["Total_Victims"] / merged_df["Total_Victims"].max() +
                           merged_df["Road_Accidents_Cases"] / merged_df["Road_Accidents_Cases"].max() +
                           merged_df["Road_Accidents_Died"] / merged_df["Road_Accidents_Died"].max()) / 3

# ----------------- CLASSIFY RISK -----------------
low = merged_df["Risk_Score"].quantile(0.33)
high = merged_df["Risk_Score"].quantile(0.66)

def classify_risk_dynamic(score):
    if score <= low:
        return "Low Risk"
    elif score <= high:
        return "Medium Risk"
    else:
        return "High Risk"

merged_df["Risk_Level"] = merged_df["Risk_Score"].apply(classify_risk_dynamic)

# ----------------- SAVE FINAL DATA -----------------
output_folder = "outputs"
os.makedirs(output_folder, exist_ok=True)
merged_df.to_csv(f"{output_folder}/final_risk_analysis_full.csv", index=False)
print(f"Final result saved to {output_folder}/final_risk_analysis_full.csv")

# ----------------- OPTIONAL: PREVIEW -----------------
print("\nFinal Risk Classification:")
print(merged_df.head())
