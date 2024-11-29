columns_for_cronbach_alpha = [
    "effectiveness",
    "feasibility",
    "envtal_conservation",
    "socioeconomic",
    "scalability",
    "sustainability",
    "com_engpa",
    "policy_alignment",
]

# Filter the DataFrame to include only rows with non-null values
df_filtered = df.dropna(subset=columns_for_cronbach_alpha)

# Convert the columns to numeric
df_filtered[columns_for_cronbach_alpha] = df_filtered[
    columns_for_cronbach_alpha
].apply(pd.to_numeric, errors="coerce")

# Calculate Cronbach's alpha
cronbach_alpha_result = cronbach_alpha(data=df_filtered[columns_for_cronbach_alpha])

# Print Cronbach's alpha
print(f"Cronbach's alpha: {cronbach_alpha_result[0]}")
