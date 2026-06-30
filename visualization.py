
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os


if not os.path.exists("charts"):
    os.makedirs("charts")


df = pd.read_csv("netflix_titles.csv")


print("FIRST 5 ROWS")
print(df.head())


print("\nDATASET INFO")
print(df.info())

print("\nDATASET SHAPE")
print(df.shape)




print("\nMISSING VALUES")
print(df.isnull().sum())


df.fillna("Unknown", inplace=True)


df.drop_duplicates(inplace=True)

print("\nData cleaning completed.")


sns.set_style("whitegrid")



plt.figure(figsize=(8, 5))
df["type"].value_counts().plot(kind="bar")

plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Type")
plt.ylabel("Count")

plt.savefig("charts/movies_vs_tvshows.png")
plt.show()



top_countries = df["country"].value_counts().head(10)

plt.figure(figsize=(10, 5))
top_countries.plot(kind="bar")

plt.title("Top 10 Countries by Netflix Content")
plt.xlabel("Country")
plt.ylabel("Number of Shows")

plt.savefig("charts/top_countries.png")
plt.show()



release_year = df["release_year"].value_counts().sort_index()

plt.figure(figsize=(12, 5))
release_year.plot(kind="line")

plt.title("Netflix Content Release Trend")
plt.xlabel("Release Year")
plt.ylabel("Number of Shows")

plt.savefig("charts/release_year_trend.png")
plt.show()


plt.figure(figsize=(10, 5))
df["rating"].value_counts().plot(kind="bar")

plt.title("Netflix Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")

plt.savefig("charts/rating_distribution.png")
plt.show()


top_genres = df["listed_in"].value_counts().head(10)

plt.figure(figsize=(12, 5))
top_genres.plot(kind="bar")

plt.title("Top 10 Genres on Netflix")
plt.xlabel("Genre")
plt.ylabel("Count")

plt.savefig("charts/genre_analysis.png")
plt.show()


plt.figure(figsize=(7, 7))

df["type"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Percentage of Movies and TV Shows")
plt.ylabel("")

plt.savefig("charts/content_percentage.png")
plt.show()


numeric_data = df[["release_year"]]

plt.figure(figsize=(6, 4))
sns.heatmap(numeric_data.corr(), annot=True)

plt.title("Correlation Heatmap")

plt.savefig("charts/heatmap.png")
plt.show()



print("\nPROJECT COMPLETED SUCCESSFULLY")
print("All charts saved in charts folder.")