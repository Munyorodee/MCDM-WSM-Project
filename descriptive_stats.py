import pandas as pd
import os
import pandas as pd

os.chdir('Desktop/4.2/Urban Water Scarcity poject/DATA/DATA CLEANING/data')

# Load each CSV file into a separate DataFrame
additional = pd.read_csv('additional.csv')
boreholes = pd.read_csv('boreholes.csv')
collaboration = pd.read_csv('collaboration.csv')
criteria_evaluation = pd.read_csv('criteria_evaluation.csv')
demand = pd.read_csv('demand.csv')

# Read and view the csv file
demand = pd.read_csv('demand.csv')
expert_background = pd.read_csv('expert_background.csv')
greywater = pd.read_csv('greywater.csv')
policy = pd.read_csv('policy.csv')
rainwater = pd.read_csv('rainwater.csv')
scenario = pd.read_csv('scenario.csv')
smart_metering = pd.read_csv('smart_metering.csv')
uncertainty = pd.read_csv('uncertainty.csv')

# Calculate descriptive statistics and export to CSV
dataframes = {
    'boreholes': boreholes,
    'collaboration': collaboration,
    'criteria_evaluation': criteria_evaluation,
    'demand': demand,
    'greywater': greywater,
    'policy': policy,
    'rainwater': rainwater,
    'smart_metering': smart_metering
}

for name, df in dataframes.items():
    descriptive_stats = df.describe()
    descriptive_stats.to_csv(f"descriptive_stats_{name}.csv", index=True)

for name, df in dataframes.items():
    descriptive_stats = df.describe()
    print(f"Descriptive statistics for {name}:")
    print(descriptive_stats)
    print("\n" + "="*50 + "\n")

    # Plot boxplots for each DataFrame with numeric columns

    import seaborn as sns
    import matplotlib.pyplot as plt

    for name, df in dataframes.items():
        numeric_df = df.select_dtypes(include='number')  # Filter to only numeric columns
        if not numeric_df.empty:
            plt.figure(figsize=(10, 6))
            sns.boxplot(data=numeric_df)
            plt.title(f'Boxplot for {name}')
            plt.xticks(rotation=45)  # Rotate x-axis labels if necessary
            plt.tight_layout()  # Adjust layout to prevent overlap
            plt.show()
        else:
            print(f"No numeric data to plot for {name}")

    ![png](output_5_0.png)
    ![png](output_5_1.png)
    ![png](output_5_2.png)
    ![png](output_5_3.png)
    ![png](output_5_4.png)
    ![png](output_5_5.png)
    ![png](output_5_6.png)
    ![png](output_5_7.png)
