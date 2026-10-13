import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from bs4 import BeautifulSoup
from pyspark.sql import SparkSession

df = pd.read_csv("sales.csv")

print(df.head())
print(df.describe())

df = df.sort_values(by="Sales", ascending=False)
print(df.head(5))

region = df.groupby("Region").agg({"Sales": "sum", "Profit": "mean"})
print(region)

print(df["Sales"].corr(df["Profit"]))

df.groupby("Month")["Sales"].sum().plot()
plt.show()

df.groupby("Region")["Sales"].sum().plot(kind="bar")
plt.show()

plt.scatter(df["Sales"], df["Profit"])
plt.show()

plt.hist(df["Profit"])
plt.show()

plt.boxplot(df["Sales"])
plt.show()

corr = df.corr()
sns.heatmap(corr, annot=True)
plt.show()

url = "https://example.com"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

items = soup.find_all("div", class_="product")

for i in items:
    try:
        name = i.find("h2").text
        price = i.find("span", class_="price").text
        rating = i.find("span", class_="rating").text
        print(name, price, rating)
    except:
        pass

spark = SparkSession.builder.appName("Sales").getOrCreate()

sdf = spark.read.csv("sales.csv", header=True, inferSchema=True)

sdf.printSchema()
sdf.show(5)

sdf.filter(sdf["Sales"] > 30000).show()

sdf.groupBy("Region").agg({"Sales": "sum", "Profit": "avg"}).show()