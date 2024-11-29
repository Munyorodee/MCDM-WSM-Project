import pandas as pd
import numpy as np

criteria_evaluation = criteria_evaluation.apply(pd.to_numeric, errors='coerce')

# Now calculate average scores for each criterion
criteria_averages = criteria_evaluation.mean()
print("Average scores for each criterion:\n", criteria_averages)

# Sum the averages to get the total average score
total_average = criteria_averages.sum()
print("\nTotal average score across all criteria:", total_average)

# Calculate normalized weights (weights should add up to 1)
criteria_weights = criteria_averages / total_average
print("\nNormalized weights for each criterion:\n", criteria_weights)

#TOTAL AVERAGE CALCULATION
# Load dataframes of interest
dataframes = {
    'boreholes': boreholes,
    'collaboration': collaboration,
    'demand': demand,
    'greywater': greywater,
    'policy': policy,
    'rainwater': rainwater,
    'smart_metering': smart_metering,
}

# Dictionary to store the averages for each alternative
alternatives_averages = {}

# Calculate the average for each column in each DataFrame
for name, df in dataframes.items():
    averages = df.mean(numeric_only=True)  # Calculate mean for each column
    alternatives_averages[name] = averages  # Store the result in the dictionary

# Print the averages for each alternative
for name, averages in alternatives_averages.items():
    print(f"Average scores for {name}:\n{averages}\n")

# NORMALIZATION OF AVERAGES

import pandas as pd

# Load dataframes of interest
dataframes = {
    'boreholes': boreholes,
    'collaboration': collaboration,
    'demand': demand,
    'greywater': greywater,
    'policy': policy,
    'rainwater': rainwater,
    'smart_metering': smart_metering,
}

# Dictionary to store the normalized averages for each alternative
normalized_averages = {}

# Calculate the average and normalize for each column in each DataFrame
for name, df in dataframes.items():
    averages = df.mean(numeric_only=True)  # Calculate mean for each column
    total_average = averages.sum()  # Calculate the total of averages

    # Normalize the averages so they sum up to 1
    if total_average != 0:  # Avoid division by zero
        normalized = averages / total_average
    else:
        normalized = averages  # If total is zero, keep as it is (all zeros)

    # Store the normalized values in the dictionary
    normalized_averages[name] = normalized

# Print the normalized averages for each alternative
for name, normalized in normalized_averages.items():
    print(f"Normalized scores for {name}:\n{normalized}\n")
