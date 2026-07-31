#🐼 Pandas Basics (Data Science & Libraries)
#Pandas is a Python library for data analysis. It builds on NumPy and makes working with tabular data (like spreadsheets or databases) much easier.

#🔹 1. Why Pandas?
#Handles structured data (rows & columns).
#Provides DataFrame (like Excel tables) and Series (like a single column).
#Easy data cleaning, filtering, grouping, merging.
#Widely used in data science, ML, and analytics.

#🔹 2. Core Data Structures
#📌 Series
#A one-dimensional labeled array.

#code

import   pandas as pd

s = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
print(s)

# Output:
# a    10
# b    20
# c    30
# d    40

#📌 DataFrame
#A two-dimensional labeled data structure (rows & columns).

#code

data = {"Name": ["Harsh", "Vivek", "Shreyas"], "Age": [21, 20, 22]}
df = pd.DataFrame(data)

print(df)

# Output:
#      Name  Age
# 0   Harsh   21
# 1   Vivek   20
# 2 Shreyas   22

#🔹 3. Basic Operations

#code

print(df.head())       # First 5 rows
print(df["Name"])      # Access column
print(df.iloc[1])      # Access row by index
print(df.describe())   # Summary statistics

#🔹 4. Common Functions

#Function	     Purpose	Example
#df.head()	     First rows	Preview data
#df.tail()	        Last rows	End of dataset
#df.info()	      Metadata	Column types
#df.describe()Stats summary	Mean, std, min, max
#df["col"]	    Select column	df["Age"]
#df.loc[0]	   Select row by label	First row
#df.iloc[2]	    Select row by index	Third row
#df.sort_values("Age")	Sort by column	Ascending ages


#🔹 5. Data Cleaning


df["Age"].fillna(df["Age"].mean(), inplace=True)  # Fill missing values
df.dropna(inplace=True)                           # Drop missing rows
df.rename(columns={"Name": "FullName"}, inplace=True)  # Rename column

#🎯 Quick Summary
#Series = 1D labeled array.
#DataFrame = 2D labeled table.
# Pandas makes data analysis simple and powerful.
# Essential for real-world projects like finance, healthcare, and ML.