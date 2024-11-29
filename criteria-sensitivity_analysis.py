# Criteria Sensitivity Analysis

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# --- Data ---
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
        'effectiveness': 0.126190,
        'feasibility': 0.128571,
        'envtal_conservation': 0.114286,
        'socioeconomic': 0.126190,
        'scalability': 0.128571,
        'sustainability': 0.126190,
        'com_engpa': 0.128571,
        'policy_alignment': 0.121429
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


# --- Functions ---
def calculate_wsm_scores(alt_weights, criteria_weights):
    """Calculates WSM scores given alternative and criteria weights."""
    final_scores = {}
    for alt_name, alt_w in alt_weights.items():
        total_score = (alt_w * criteria_weights).sum()
        final_scores[alt_name] = total_score
    return pd.Series(final_scores)


# Calculate the original scores
original_scores = calculate_wsm_scores(alternative_weights, criteria_weights)

# Sensitivity Analysis with 10% Perturbation
perturbation_factor = 0.1  # 10% perturbation
sensitivity_results = {'Original': original_scores}

for criterion in criteria_weights.index:
    # Increase weight by 10%
    increased_weights = criteria_weights.copy()
    increased_weights[criterion] *= (1 + perturbation_factor)
    increased_weights /= increased_weights.sum()  # Normalize to keep sum = 1
    increased_scores = calculate_wsm_scores(alternative_weights, increased_weights)
    sensitivity_results[f'{criterion}_+10%'] = increased_scores

    # Decrease weight by 10%
    decreased_weights = criteria_weights.copy()
    decreased_weights[criterion] *= (1 - perturbation_factor)
    decreased_weights /= decreased_weights.sum()  # Normalize to keep sum = 1
    decreased_scores = calculate_wsm_scores(alternative_weights, decreased_weights)
    sensitivity_results[f'{criterion}_-10%'] = decreased_scores

# Combine results into a DataFrame for easy plotting
sensitivity_df = pd.DataFrame(sensitivity_results)

# --- Plotting ---
# Melt the DataFrame for seaborn plotting
melted_df = sensitivity_df.reset_index().melt(id_vars='index', var_name='Perturbation', value_name='Score')

# Line Plot
plt.figure(figsize=(14, 8))
sns.lineplot(x='Perturbation', y='Score', hue='index', data=melted_df, marker='o')
plt.xticks(rotation=45, ha='right')
plt.ylabel('Weighted Sum Score')
plt.xlabel('Criteria Perturbation')
plt.title('Sensitivity Analysis - Impact of 10% Perturbation on WSM Scores')
plt.legend(title='Alternatives', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()


# --- Recalculate Rankings ---
def calculate_rankings(scores_df):
    """Converts scores into rankings (lower rank = higher preference)."""
    return scores_df.rank(ascending=False, axis=0, method='min')


# Calculate rankings for original and perturbed scores
rankings_df = calculate_rankings(sensitivity_df)

# --- Calculate Rank Changes ---
# Calculate rank differences from the original rankings
rank_changes = rankings_df.sub(rankings_df['Original'], axis=0)

# --- Plot the Effects of Perturbation ---
# Prepare melted DataFrame for plotting rank shifts
rank_melted_df = rank_changes.reset_index().melt(
    id_vars='index', var_name='Perturbation', value_name='Rank Change'
)

# Line Plot of Rank Changes
plt.figure(figsize=(14, 8))
sns.lineplot(x='Perturbation', y='Rank Change', hue='index', data=rank_melted_df, marker='o')
plt.axhline(0, color='gray', linestyle='--', linewidth=1)  # Baseline for no rank change
plt.xticks(rotation=45, ha='right')
plt.ylabel('Rank Change')
plt.xlabel('Criteria Perturbation')
plt.title('Sensitivity Analysis - Rank Changes due to Perturbation')
plt.legend(title='Alternatives', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# --- Summarize Results ---
print("=== WSM Rankings Before and After Perturbation ===")
print(rankings_df)

print("\n=== Rank Changes Due to Perturbation ===")
print(rank_changes)
![png](output_20_1.png)
![png](output_20_2.png)
![png](output_20_3.png)
