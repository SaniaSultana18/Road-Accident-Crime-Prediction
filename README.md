# 🚨 Road Accident & Crime Risk Analysis

This project analyzes road accident and crime data across India, calculates risk scores for each state/UT, and visualizes the results in an interactive dashboard.

---

## 🌐 Live Demo
You can view the live app here: [Open Dashboard](https://road-accident-crime-prediction-rbiutpah4nnqvnf8sej6wa.streamlit.app)

---

## 📂 Project Structure
- `main.py` : Processes datasets, calculates risk scores, and generates `final_risk_analysis.csv`.
- `app.py` : Streamlit dashboard to visualize and explore risk metrics.
- `data/` : Input datasets
  - Crime datasets (POCSO & IPC related)
  - Road accidents data (2022)
- `outputs/` : Generated CSVs and charts
  - `final_risk_analysis.csv` : Combined and processed dataset
  - Charts like risk level distribution, crime distribution, road accident stats
- `requirements.txt` : Python dependencies for running the project

---

## 📊 Features
1. **Merged Data Preview**: See the combined crime and road accident data.  
2. **Key Metrics**: Total states, crime cases, child/adult victims, road accident cases and deaths.  
3. **Crime Distribution**: Pie chart of child vs adult victims.  
4. **Risk Level Distribution**: Bar chart showing states classified as Low, Medium, High risk.  
5. **Top 10 High Risk States**: Quick view of the states with highest risk scores.  
6. **Road Accidents: Cases vs Deaths**: Visual comparison for each state.  
7. **Check Risk Details by State/UT**: Select a state to view detailed statistics.

---

## ⚙️ How to Run Locally
1. Clone the repository:
git clone https://github.com/SaniaSultana18/Road-Accident-Crime-Prediction.git

cd Road-Accident-Crime-Prediction   

2. Install dependencies:

   pip install -r requirements.txt

3. Run the Streamlit app:

   streamlit run app.py

