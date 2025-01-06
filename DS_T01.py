import pandas as pd
import matplotlib.pyplot as plt

file_path = r"C:\clg notes sec\SEM 3\API_SP.POP.TOTL_DS2_en_csv_v2_900.csv"
data = pd.read_csv(file_path, skiprows=4)  
print(data.head())

year = 2020
filtered_data = data[["Country Name", str(year)]].dropna()

filtered_data.columns = ["Country", "Population"]

top_countries = filtered_data.sort_values("Population", ascending=False).head(10)

plt.figure(figsize=(12, 6))
plt.bar(top_countries["Country"], top_countries["Population"] / 1e6, color="skyblue", edgecolor="black")
plt.title(f"Top 10 Countries by Population in {year}", fontsize=16)
plt.xlabel("Country", fontsize=12)
plt.ylabel("Population (in Millions)", fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()


plt.figure(figsize=(12, 6))
plt.hist(filtered_data["Population"] / 1e6, bins=15, color="coral", edgecolor="black")
plt.title(f"Population Distribution Across Countries ({year})", fontsize=16)
plt.xlabel("Population (in Millions)", fontsize=12)
plt.ylabel("Number of Countries", fontsize=12)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
plt.show()
