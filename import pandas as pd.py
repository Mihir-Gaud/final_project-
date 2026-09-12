import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv(r"c:\Users\admin\Downloads\happiness.csv")

print("First 5 Rows")
print(df.head())

print("\nDataset Shape")
print(df.shape)

print("\nColumns")
print(df.columns)

print("\nMissing Values")
print(df.isnull().sum())

print("\nStatistics")
print(df.describe())

# Top 10 Happiest Countries
top10 = df.sort_values("Happiness Score", ascending=False).head(10)

print("\nTop 10 Happiest Countries")
print(top10[['Country','Happiness Score']])

# Average Happiness Score
print("\nAverage Happiness Score")
print(df["Happiness Score"].mean())

sns.set_style("whitegrid")

# ------------------------------------
# 1 Top 10 Countries
# ------------------------------------

plt.figure(figsize=(10,5))

plt.bar(top10["Country"], top10["Happiness Score"])

plt.title("Top 10 Happiest Countries")

plt.xlabel("Country")

plt.ylabel("Happiness Score")

plt.xticks(rotation=45)

plt.show()

# ------------------------------------
# 2 Histogram
# ------------------------------------

plt.figure(figsize=(7,5))

plt.hist(df["Happiness Score"], bins=10)

plt.title("Happiness Score Distribution")

plt.xlabel("Score")

plt.ylabel("Countries")

plt.show()

# ------------------------------------
# 3 Scatter Plot
# ------------------------------------

plt.figure(figsize=(7,5))

plt.scatter(df["GDP per Capita"],
            df["Happiness Score"])

plt.xlabel("GDP per Capita")

plt.ylabel("Happiness Score")

plt.title("GDP vs Happiness")

plt.show()

# ------------------------------------
# 4 Pie Chart
# ------------------------------------

top5 = top10.head(5)

plt.figure(figsize=(6,6))

plt.pie(
top5["Happiness Score"],
labels=top5["Country"],
autopct="%1.1f%%"
)

plt.title("Top 5 Happiness Share")

plt.show()

# ------------------------------------
# 5 Correlation Heatmap
# ------------------------------------

plt.figure(figsize=(6,5))

numeric=df.select_dtypes(include='number')

sns.heatmap(numeric.corr(),
annot=True)

plt.title("Correlation Heatmap")

plt.show()