#                                                                          Data Analysis with Python
# What is Data Analysis
# a process of inspecting, cleansing, transforming and modeling data with the goal of discovering useful information
# informing conclusion and supporting decision-making.

#                                                                          The Data Analysis Process
# Data Extraction ------> Data Cleaning -------------------> Data Wrangling -------------------------> Analysis ------------------------------> Action
# SQL                    # Missing values and empty data   # Hierarchical Data                      # Exploration                       # Building Machine Learning Models
# Scrapping              # Data imputation                 # Handling categorical data              # Building statistical models       # Feature Engineering
# File Formats           # Incorrect types                 # Reshaping and transforming structures  # Visualization and representations # Moving ML into production
# - CSV
# - JSON
# - XML
# Consulting APIs        # Incorrect or invalid values     # Indexing data for quick access         # Correlation vs Causation analysis # Building ETL pipelines
# Buying Data            # Outliers and non relevant data  # Merging, combining and joining data    # Hypothesis testing                # Live dashboard and reporting
# Distributed Databases  # Statistical sanitization                                                 # Statistical analysis              # Decision making and real-life tests
                                                                                                    # Reporting

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# %matplotlib inline
# !head data/file_name.csv  # opening file
# sales = pd.read_csv(      # reading file
#   'data/sales_data.csv',
#    parse_dates=['Date'])

# Checking data look 
# filename.head()
# filename.shape
# filename.info()
# filename.describe()

# sales['Calculated_Cost'] = sales['Order_Quantity'] * sales['Unit_Cost']

# sales['Calculated_Cost'].head()
# (sales['Calculated_Cost'] != sales['Cost']).sum() # checking if there are diffrences 

# We can see the relationship between Cost and Profit using a scatter plot:
# sales.plot(kind='scatter', x='Calculated_Cost', y='Profit', figsize=(6,6))

#Calculated_Revenue = Cost + Sales
# sales['Calculated_Revenue'] = sales['Cost'] + sales['Profit']

#sales['Calculated_Revenue'].head()

# (sales['Calculated_Revenue'] != sales['Revenue']).sum() # checking diff

# Modifying price by adding diff %:
# sales['Unit_Price'].head()
# 0    120
# 1    120
# 2    120
# 3    120
# 4    120
# Name: Unit_Price, dtype: int64

# sales['Unit_Price'] *= 1.03
# sales['Unit_Price'].head()
# 0    123.6
# 1    123.6
# 2    123.6
# 3    123.6
# 4    123.6
# Name: Unit_Price, dtype: float64

# Get the mean revenue of the specific sales group
#sales.loc[sales['Age_Group'] == 'specific age group', 'Revenue'].mean()

# How many records belong to Age Group x or Adults y?
# sales.loc[(sales['Age_Group'] == 'x') | (sales['Age_Group'] == 'y')].shape[0]

# Increase the revenue by specific % to every sale made in specific country
# sales.loc[sales['Country'] == 'specific country', 'Revenue'] *= 1.1
# sales.loc[sales['Country'] == 'specific country', 'Revenue'].head()

# we can analyze specific column 
# df['specific_column_aqhdjq'].describe()
# df['specific_column_aqhdjq'].median()
# ax = df['specific_column_aqhdjq'].value_counts().plot(kind='bar', figsize=(14,6)) # creacting bar chart
# ax.set_ylabel('Number of something') # setting name of left side

#                                                                              Selection & Indexing:
# gets the records of the customer with lastname 
# df.loc[df['customer_lastname'] == 'HANSEN']
# 

























