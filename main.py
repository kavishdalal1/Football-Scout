import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
players = pd.read_csv(r"/Users/kavishdalal/Downloads/archive/players_data_light-2024_2025.csv")
players = players.dropna(subset="Nation")
players = players.dropna(axis=1,how="all")
a = players["Gls"].max()
b = players.loc[players["Gls"].idxmax()]
print("The top scorer of the 24-25 season is ",b["Player"],"with a goal tally of ",a)
c = players["Ast"].max()
d = players.loc[players["Ast"].idxmax()]
print("The top playmaker of the 24-25 season is ",d["Player"],"with",c,"assists.")
#Segerating the players based on position
forwards = players[players["Pos"].str.contains("FW")]
defenders = players[players["Pos"].str.contains("DF")]
midfielders = players[players["Pos"].str.contains("MF")]
goalkeeper = players[players["Pos"] == "GK"]
#Using a formula rate players in their respective position
forwards["Score"] = 0.4*forwards["Gls"] + 0.2*forwards["Ast"] + 0.2*forwards["xG"] + 0.2*forwards["SoT%"]
midfielders["Score"] = 0.4*midfielders["Ast"] + 0.2*midfielders["xAG"] + 0.2*midfielders["PrgP"] + 0.2*midfielders["Gls"]
defenders["Score"] = 0.4*defenders["Tkl%"] + 0.3*defenders["Blocks_stats_defense"] + 0.3*defenders["Int"]
goalkeeper["Score"] = 0.4*goalkeeper["Saves"] + 0.3*goalkeeper["CS"] + 0.3*goalkeeper["PSxG+/-"]
#Plotting top players of their respective position
top_fw = forwards.nlargest(20,"Score")
plt.bar(top_fw["Player"],top_fw["Score"])
plt.xlabel("Forward Name")
plt.ylabel("Forward Score")
plt.title("Top 20 Forwards in the 24-25 season")
plt.xticks(rotation=45,ha="right")
plt.tight_layout()
plt.savefig("top_forwards.png")
plt.show()

top_mf = midfielders.nlargest(20,"Score")
plt.bar(top_mf["Player"],top_mf["Score"])
plt.xlabel("Midfielder Name")
plt.ylabel("Midfielder Score")
plt.title("Top Midfielders in the 24-25 season")
plt.xticks(rotation=45,ha="right")
plt.tight_layout()
plt.savefig("top_mf.png")
plt.show()

top_df = defenders.nlargest(20,"Score")
plt.bar(top_df["Player"],top_df["Score"])
plt.xlabel("Defender Name")
plt.ylabel("Defender Score")
plt.title("Top 20 Defenders in the 24-25 season")
plt.xticks(rotation=45,ha="right")
plt.tight_layout()
plt.savefig("top_def.png")
plt.show()

top_gk = goalkeeper.nlargest(20,"Score")
plt.bar(top_gk["Player"],top_gk["Score"])
plt.xlabel("Goalkeeper Name")
plt.ylabel("Goalkeeper Score")
plt.title("Top 20 Goalkeepers in the 24-25 season")
plt.xticks(rotation=45,ha="right")
plt.tight_layout()
plt.savefig("top_gk.png")
plt.show()

#Hidden Gem Analysis

young_forwards = forwards[forwards["Age"]<=23]
young_defenders = defenders[defenders["Age"]<=23]
young_midfielders = midfielders[midfielders["Age"]<=23]
young_goalkeeper = goalkeeper[goalkeeper["Age"]<=23]

hidden_fw = young_forwards.nlargest(10,"Score")
hidden_df = young_defenders.nlargest(10,"Score")
hidden_mf = young_midfielders.nlargest(10,"Score")
hidden_gk = young_goalkeeper.nlargest(10,"Score")

print("The young superstar forwards of the 24-25 season are")
print(hidden_fw["Player"])
print("The young superstar midfielders are")
print(hidden_mf["Player"])
print("The young superstar defenders of the 24-25 season are")
print(hidden_df["Player"])
print("The young superstar goalkeepers are")
print(hidden_gk["Player"])

#Best Finisher
forwards["Finishing"] = forwards["Gls"] - forwards["xG"]
best_finisher = forwards.loc[forwards["Finishing"].idxmax()]
print("The best finisher of the 24-25 season is : ",best_finisher["Player"])

#Squad Segregation
for_sq = forwards.groupby("Squad")["Score"].mean()
df_sq = defenders.groupby("Squad")["Score"].mean()

best_attacking_team = for_sq.idxmax()
best_defensive_team = df_sq.idxmax()
print("The best attacking team in Europe in the 24-25 season is ",best_attacking_team)
print("The best defensive team in Europe in the 24-25 season is ",best_defensive_team)

#Answering Some Popular Questions Using Heatmaps

cols = ["Gls", "xG", "Sh", "SoT%", "Ast"]
corr = forwards[cols].corr()
plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Relationship Between Goals, xG and Shooting Metrics")
plt.tight_layout()
plt.savefig("xg_goals_heatmap.png")
plt.show()

cols = ["Ast", "xAG", "KP", "PrgP"]
corr = midfielders[cols].corr()
plt.figure(figsize=(8,6))
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Relationship Between Assists and Creativity Metrics")
plt.tight_layout()
plt.savefig("assists_heatmap.png")
plt.show()

#Analysing The Leagues

leagues_fw = forwards.groupby("Comp")["Score"].mean()
leagues_df = defenders.groupby("Comp")["Score"].mean()
best_fw_league = leagues_fw.idxmax()
best_df_league = leagues_df.idxmax()
print("The best attacking league in Europe in 24-25 season is ",best_fw_league)
print("The best defensive league in Europe in the 24-25 season is ",best_df_league)

# The "Age" factor
plt.scatter(forwards["Age"],forwards["Score"])
plt.xlabel("Age")
plt.ylabel("Forward Score")
plt.title("Age vs Forward Score")
plt.savefig("age_vs_forward_score.png")

plt.show()

plt.scatter(defenders["Age"],defenders["Score"])
plt.xlabel("Age")
plt.ylabel("Defender Score")
plt.title("Age vs Defender Score")
plt.savefig("age_vs_defender_score.png")
plt.show()