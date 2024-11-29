import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define the criteria weights (based on normalized values provided)
criteria_weights = pd.Series({
    'effectiveness': 0.132385,
    'feasibility': 0.129103,
    'envtal_conservation': 0.120350,
    'socioeconomic': 0.115974,
    'scalability': 0.120350,
    'sustainability': 0.128009,
    'com_engpa': 0.128009,
    'policy_alignment': 0.125821
})

# Step 2: Define the decision matrix with alternatives (based on your provided weights)
decision_matrix = pd.DataFrame({
    'effectiveness': [0.118938, 0.127586, 0.143631, 0.129070, 0.128878, 0.130539, 0.129187],
    'feasibility': [0.127021, 0.128736, 0.146341, 0.125581, 0.128878, 0.125749, 0.135167],
    'envtal_conservation': [0.116628, 0.114943, 0.130081, 0.122093, 0.122912, 0.118563, 0.117225],
    'socioeconomic': [0.123557, 0.128736, 0.143631, 0.126744, 0.124105, 0.124551, 0.125598],
    'scalability': [0.128176, 0.125287, 0.146341, 0.123256, 0.119332, 0.124551, 0.120813],
    'sustainability': [0.122402, 0.125287, 0.143631, 0.120930, 0.126492, 0.120958, 0.125598],
    'com_engpa': [0.135104, 0.126437, 0.146341, 0.126744, 0.124105, 0.130539, 0.118421],
    'policy_alignment': [0.128176, 0.122989, 0.000000, 0.125581, 0.125298, 0.124551, 0.127990]
}, index=['boreholes', 'collaboration', 'demand', 'greywater', 'policy', 'rainwater', 'smart_metering'])

# Step 3: Normalize the decision matrix
normalized_matrix = decision_matrix / np.sqrt((decision_matrix**2).sum())

# Step 4: Calculate the weighted normalized decision matrix
weighted_matrix = normalized_matrix * criteria_weights

# Step 5: Determine the ideal (best) and anti-ideal (worst) solutions
ideal_solution = weighted_matrix.max()  # Best values (assuming all criteria are benefit criteria)
anti_ideal_solution = weighted_matrix.min()  # Worst values

# Step 6: Calculate the Euclidean distance from the ideal and anti-ideal solutions for each alternative
dist_to_ideal = np.sqrt(((weighted_matrix - ideal_solution)**2).sum(axis=1))
dist_to_anti_ideal = np.sqrt(((weighted_matrix - anti_ideal_solution)**2).sum(axis=1))

# Step 7: Calculate the relative closeness to the ideal solution
relative_closeness = dist_to_anti_ideal / (dist_to_ideal + dist_to_anti_ideal)

# Step 8: Rank alternatives based on relative closeness
ranked_alternatives_topsis = relative_closeness.sort_values(ascending=False)

# Display the ranked alternatives
print("Final Ranking of Alternatives based on TOPSIS:\n", ranked_alternatives_topsis)

# Visualize the ranking using a horizontal bar graph
plt.figure(figsize=(10, 6))
plt.barh(ranked_alternatives_topsis.index, ranked_alternatives_topsis.values, color='skyblue')
plt.xlabel('Relative Closeness to Ideal Solution')
plt.ylabel('Alternatives')
plt.title('Final Ranking of Alternatives based on TOPSIS')
plt.gca().invert_yaxis()  # Invert y-axis to show highest rank at the top
plt.xlim(0.2, 0.75)
plt.show()
![png](output_15_1.png)
