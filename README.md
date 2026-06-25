⚽ Football Scout Analytics

A Python-based football analytics project that evaluates player performance across Europe's top leagues using statistical analysis and custom scoring models.

This project uses Pandas, NumPy, Matplotlib, and Seaborn to clean data, analyze player statistics, identify hidden talents, compare leagues and clubs, and visualize key football insights from the 2024–25 season.

---

📊 Features

- Cleans and preprocesses player datasets
- Separates players into:
  - Forwards
  - Midfielders
  - Defenders
  - Goalkeepers
- Creates a custom performance score for every position
- Identifies:
  - Top 20 players in every position
  - Best finisher
  - Hidden gems (Under-23 players)
- Finds:
  - Best attacking team
  - Best defensive team
  - Best attacking league
  - Best defensive league
- Performs correlation analysis using heatmaps
- Studies the relationship between player age and performance
- Generates professional visualizations automatically

---

🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

📂 Dataset

Dataset used:

FBref Player Statistics (2024–25 Season)

The dataset contains player statistics including:

- Goals
- Assists
- Expected Goals (xG)
- Expected Assists (xAG)
- Progressive Passes
- Tackles
- Blocks
- Interceptions
- Saves
- Clean Sheets
- Shot Accuracy
- Age
- Position
- League
- Club

---

📈 Visualizations

Top 20 Forwards

"Top Forwards" (top_forwards.png)

---

Top 20 Midfielders

"Top Midfielders" (top_mf.png)

---

Top 20 Defenders

"Top Defenders" (top_def.png)

---

Top 20 Goalkeepers

"Top Goalkeepers" (top_gk.png)

---

Goals vs Expected Goals Correlation

"Goals Heatmap" (xg_goals_heatmap.png)

---

Creativity Metrics Correlation

"Creativity Heatmap" (assists_heatmap.png)

---

Age vs Forward Performance

"Age vs Forward Score" (age_vs_forward_score.png)

---

Age vs Defender Performance

"Age vs Defender Score" (age_vs_defender_score.png)

---

🏆 Key Findings

Top Performer Analysis

- Top Scorer of the season
- Top Playmaker
- Best Finisher (Goals − xG)

Hidden Gem Analysis

The project identifies the best Under-23 players across:

- Forwards
- Midfielders
- Defenders
- Goalkeepers

Team Analysis

- Best attacking club based on average forward scores
- Best defensive club based on average defender scores

League Analysis

- Best attacking league
- Best defensive league

Statistical Analysis

The project investigates questions such as:

- Does Expected Goals (xG) actually predict goals?
- Do creative metrics strongly correlate with assists?
- Does player age significantly affect performance?

---

▶️ How to Run

Clone the repository

git clone https://github.com/YOUR_USERNAME/Football-Scout.git

Install dependencies

pip install -r requirements.txt

Run the project

python main.py

---

📁 Project Structure

Football-Scout/

├── main.py
├── README.md
├── requirements.txt
├── top_forwards.png
├── top_mf.png
├── top_def.png
├── top_gk.png
├── xg_goals_heatmap.png
├── assists_heatmap.png
├── age_vs_forward_score.png
├── age_vs_defender_score.png

---

🚀 Future Improvements

- Interactive Streamlit dashboard
- Transfer recommendation system
- Player similarity analysis
- Radar charts for player comparison
- Machine Learning based player rating model
- Team of the Season generator

---

👨‍💻 Author

Kavish Dalal

Second-year B.Tech student passionate about Data Analytics, Python, and Football Analytics.
