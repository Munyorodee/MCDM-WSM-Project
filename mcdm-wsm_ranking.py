# Ranking of Alternatives based on WSM:
import pandas as pd

# Step 1: Define normalized weights for each criterion based on your provided data
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

# Step 2: Define weights for each alternative based on provided weights
alternative_weights = {
    'boreholes': pd.Series({
        'effectiveness': 0.118938,
        'feasibility': 0.127021,
        'envtal_conservation': 0.116628,
        'socioeconomic': 0.123557,
        'scalability': 0.128176,
        'sustainability': 0.122402,
        'com_engpa': 0.135104,
        'policy_alignment': 0.128176
    }),
    'collaboration': pd.Series({
        'effectiveness': 0.127586,
        'feasibility': 0.128736,
        'envtal_conservation': 0.114943,
        'socioeconomic': 0.128736,
        'scalability': 0.125287,
        'sustainability': 0.125287,
        'com_engpa': 0.126437,
        'policy_alignment': 0.122989
    }),
    'demand': pd.Series({
        'effectiveness': 0.143631,
        'feasibility': 0.146341,
        'envtal_conservation': 0.130081,
        'socioeconomic': 0.143631,
        'scalability': 0.146341,
        'sustainability': 0.143631,
        'com_engpa': 0.146341,
        'policy_alignment': 0
    }),
    'greywater': pd.Series({
        'effectiveness': 0.129070,
        'feasibility': 0.125581,
        'envtal_conservation': 0.122093,
        'socioeconomic': 0.126744,
        'scalability': 0.123256,
        'sustainability': 0.120930,
        'com_engpa': 0.126744,
        'policy_alignment': 0.125581
    }),
    'policy': pd.Series({
        'effectiveness': 0.128878,
        'feasibility': 0.128878,
        'envtal_conservation': 0.122912,
        'socioeconomic': 0.124105,
        'scalability': 0.119332,
        'sustainability': 0.126492,
        'com_engpa': 0.124105,
        'policy_alignment': 0.125298
    }),
    'rainwater': pd.Series({
        'effectiveness': 0.130539,
        'feasibility': 0.125749,
        'envtal_conservation': 0.118563,
        'socioeconomic': 0.124551,
        'scalability': 0.124551,
        'sustainability': 0.120958,
        'com_engpa': 0.130539,
        'policy_alignment': 0.124551
    }),
    'smart_metering': pd.Series({
        'effectiveness': 0.129187,
        'feasibility': 0.135167,
        'envtal_conservation': 0.117225,
        'socioeconomic': 0.125598,
        'scalability': 0.120813,
        'sustainability': 0.125598,
        'com_engpa': 0.118421,
        'policy_alignment': 0.127990
    })
}

# Step 3: Calculate the weighted sum score for each alternative
final_scores = {alt_name: round((alt_weights * criteria_weights).sum(), 6)
                for alt_name, alt_weights in alternative_weights.items()}

# Step 4: Convert the final scores to a pandas Series and rank them
ranked_alternatives = pd.Series(final_scores).sort_values(ascending=False)

# Display the ranked alternatives
print("Final Ranking of Alternatives based on WSM:\n", ranked_alternatives)

# RANKINGS BAR CHART

import pandas as pd
import matplotlib.pyplot as plt

# Visualize the ranking using a horizontal bar graph
plt.figure(figsize=(10, 6))
plt.barh(ranked_alternatives.index, ranked_alternatives.values)
plt.xlabel('Weighted Sum Score')
plt.ylabel('Alternatives')
plt.title('Final Ranking of Alternatives based on WSM')
plt.gca().invert_yaxis()  # Invert y-axis to show highest rank at the top
plt.xlim(0.124, 0.126)
plt.show()
![png](output_13_0.png)
