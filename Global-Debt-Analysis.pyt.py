import pandas as pd
import matplotlib.pyplot as plt

# STEP 1: Load data
df = pd.read_csv("debt_data.csv")

# STEP 2: Convert wide → long
df_long = df.melt(id_vars=["Country Name"], 
                  var_name="Year", 
                  value_name="Debt")

df_long = df_long.dropna()
df_long["Year"] = df_long["Year"].astype(int)

print(df_long.head())
print(df_long.shape)

# STEP 3: Top countries by debt
top_countries = df_long.groupby("Country Name")["Debt"].sum().sort_values(ascending=False)

print(top_countries.head(10))

# STEP 4: Graph
top_countries.head(10).plot(kind='bar')

plt.title("Top 10 Countries by Total Debt")
plt.xlabel("Country")
plt.ylabel("Total Debt")
plt.xticks(rotation=45)

plt.show()

# 🔥 STEP 4: ADD YOUR NEW CODE HERE (AT THE BOTTOM)

# Debt trend over time
debt_trend = df_long.groupby("Year")["Debt"].sum()

print(debt_trend.head())

debt_trend.plot()

plt.title("Global Debt Trend Over Time")
plt.xlabel("Year")
plt.ylabel("Total Debt")

plt.show()


# High-risk countries (highest debt values)
high_risk = df_long.sort_values(by="Debt", ascending=False)

print(high_risk.head(10))

# visualize high risk countriers

high_risk_top = high_risk.head(10)

high_risk_top.plot(x="Country Name", y="Debt", kind="bar")

plt.title("Top High-Risk Countries by Debt")
plt.xlabel("Country")
plt.ylabel("Debt")

plt.xticks(rotation=45)
plt.show()


