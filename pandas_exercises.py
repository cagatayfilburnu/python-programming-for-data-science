#####################################################
#     Pandas Exercises with Titanic and Tips
#####################################################

# Import libraries and define titanic dataset.
import numpy as np
import pandas as pd
import seaborn as sns
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 500)
df = sns.load_dataset("titanic")
df.info()
df.head()

# Find the number of female and male passengers.
df["sex"].value_counts()

# Find the number of unique values for each column.
for col in df.columns:
    print(f"Number of unique values in {col}: {df[col].nunique()}")
    print("#################################")

# Find the number of unique values of the "pclass" variable
df["pclass"].unique()
df["pclass"].nunique()

# Find the number of unique values of "pclass" and "parch" variables.
df["pclass"].nunique()
df["parch"].nunique()

# Check the type of the "embarked" variable. Change its type to Category and check again.
df["embarked"].value_counts()  # object, int64
df["embarked"] = df["embarked"].astype("category")
df.info()

# Show all information of embarked value that is "C".
df.loc[(df["embarked"]) == "C"].head()

# Show all information of embarked value that is not "S".
df.loc[(df["embarked"] != "S")].head()

# Show all information of passengers who is lower than 30 years old and female.
df.loc[(df["age"] < 30) & (df["sex"] == "female")].head()
df.loc[(df["age"] < 30) & (df["sex"] == "female")].count()

# Show all information of passengers who is more than 500 Fare or grater than 70 years old.
df.loc[(df["fare"] > 500) | (df["age"] > 70)].head()
df.loc[(df["fare"] > 500) | (df["age"] > 70)].count()

# Find the sum of the null values in each variable.
df.isnull().values.any()
df.isnull().sum()  # null values for every variable

# Drop the "who" variable in dataset.
df.drop("who", axis=1).head()

# Fill the empty values in the "deck" variable with the most repeated value (mode) of the "deck" variable.
df["deck"].fillna(df["deck"].mode()[0], inplace=True)
df.deck.isnull().any()  # control

# Fill the empty values in the "age" variable with the median.
df["age"].fillna(df["age"].median(), inplace=True)
df.age.isnull().any()  # control

# Find the sum, count, mean values of the "survived" variable in the breakdown of "pclass" and "sex" variables.
df.groupby(["sex", "pclass"]).agg({"survived": ["sum", "count", "mean"]})

# Define a function that assign "1" passengers who is lower than 30 years old and other ones "0".
# Create a variable in dataset with function that is created by you.
# (use apply and lambda)*
def separator_for_age(arg):
    if arg < 30:
        return 1
    else:
        return 0


df["age_flag"] = df["age"].apply(lambda x: separator_for_age(x))
df.head()

# Define Tips dataset from Seaborn.
df_tips = sns.load_dataset("Tips")
df_tips.head()
df_tips.info()

# Find the sum, min, max and average of the "total_bill" values
# According to the categories of the "time" and "day" variable.
df_tips.groupby(["time"]).agg({"total_bill": ["sum", "min", "max", "mean"]})

# Find the sum, min, max and average of "total_bill" values by "days" and "time".
df_tips.groupby(["day", "time"]).agg({"total_bill": ["sum", "min", "max", "mean"]})

# Find the sum, min, max & average of the "total_bill" and "type" values of the Female customers and Lunch for "day".
df_tips.head()
df_tips.loc[(df_tips["sex"] == "Female") &
            (df_tips["time"] == "Lunch")].groupby(["day"]).agg({"tip": ["sum", "min", "max", "mean"],
                                                                "total_bill": ["sum", "min", "max", "mean"]})

# Find the average of orders with "size" less than 3 and "total_bill" greater than 10.
df_tips.loc[(df_tips["size"] < 3) & (df_tips["total_bill"] > 10)].mean(numeric_only=True)

# Create a new variable that is "total_bill_tip_sum" and sum of "total_bill" and "tip".
df_tips["total_bill_tip_sum"] = df_tips["total_bill"] + df_tips["tip"]
df_tips.head()

# Last, sort the dataset according to our new variable that is "total_bill_tip_sum" from smallest to largest.
# Create a new variable and assign to first 30 people from sorted dataset.
df_tips.sort_values(by=["total_bill_tip_sum"], ascending=True)
df_new_tips = df_tips.head(30)
df_new_tips.count()
