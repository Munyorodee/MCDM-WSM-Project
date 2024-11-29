# SCENARIO ANALYSIS
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load data
df = pd.read_csv('scenario.csv')

# 1. Descriptive Statistics
scenario_summary = df[['drought_implications', 'urbanization_population', 'change_changes', 'economic_political-instability']].describe()
print("Descriptive Statistics:\n", scenario_summary)

# 2. Frequency Analysis
for column in ['drought_implications', 'urbanization_population', 'change_changes', 'economic_political-instability']:
    print(f"\nFrequency distribution for {column}:")
    print(df[column].value_counts())
