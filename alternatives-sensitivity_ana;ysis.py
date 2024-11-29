import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# Function to calculate WSM scores
def calculate_wsm_scores(alt_weights, criteria_weights):
    """Calculates WSM scores for all alternatives given their weights and criteria."""
    return {alt: (weights * criteria_weights).sum() for alt, weights in alt_weights.items()}


# --- Perturbation Sensitivity Analysis ---
perturbation_factor = 0.1  # 10% perturbation

# Initialize storage for results
sensitivity_results = {'Original': calculate_wsm_scores(alternative_weights, criteria_weights)}

# Perform sensitivity analysis for each alternative and its respective criterion
for alternative, alt_weights in alternative_weights.items():
    for criterion in criteria_weights.index:
        # Perturb criterion weight for the alternative
        for direction, factor in [('+10%', 1 + perturbation_factor), ('-10%', 1 - perturbation_factor)]:
            perturbed_alt_weights = alternative_weights.copy()

            # Apply perturbation to the specific criterion for the alternative
            perturbed_alt_weights[alternative][criterion] *= factor
            perturbed_alt_weights[alternative] /= perturbed_alt_weights[alternative].sum()  # Normalize

            # Calculate WSM scores after perturbation
            perturbed_scores = calculate_wsm_scores(perturbed_alt_weights, criteria_weights)
            sensitivity_results[f'{alternative}_{criterion}_{direction}'] = perturbed_scores

# --- Results Summary ---
# Combine results into a DataFrame
sensitivity_df = pd.DataFrame(sensitivity_results)

# Recalculate rankings for original and perturbed scores
ranking_df = sensitivity_df.rank(ascending=False, axis=0)

# Calculate rank changes compared to the original rankings
rank_changes_df = ranking_df.sub(ranking_df['Original'], axis=0)

# --- Plotting ---
# Prepare data for plotting
melted_rank_changes = rank_changes_df.reset_index().melt(
    id_vars='index', var_name='Perturbation', value_name='Rank Change'
)

# Line Plot for Rank Changes
plt.figure(figsize=(14, 8))
sns.lineplot(data=melted_rank_changes, x='Perturbation', y='Rank Change', hue='index', marker='o')
plt.axhline(0, color='gray', linestyle='--', linewidth=1)  # Baseline for no rank change
plt.xticks(rotation=45, ha='right')
plt.ylabel('Rank Change')
plt.xlabel('Alternative-Criterion Perturbation')
plt.title('Sensitivity Analysis: Rank Changes Due to Alternative and Criterion Perturbation')
plt.legend(title='Alternatives', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# --- Summary Outputs ---
print("=== WSM Rankings Before and After Sensitivity Analysis ===")
print(ranking_df)

print("\n=== Rank Changes Due to Sensitivity Analysis ===")
print(rank_changes_df)
![png](output_21_0.png)
![png](output_21_1.png)
