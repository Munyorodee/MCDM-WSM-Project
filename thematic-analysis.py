# WORDCLOUD 1

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load the data from additional.csv
df = pd.read_csv('additional.csv')

# Remove entries with NaN in the 'areas_of_improvement' column
df = df.dropna(subset=['recommended_strategy'])

# Extract the text data from the causes_of_waterscarcity column
all_responses = ' '.join(df['recommended_strategy'].astype(str).tolist())

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_responses)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
![png](output_16_0.png)

# wordcloud 2

import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load the data from additional.csv
df = pd.read_csv('additional.csv')

# Remove entries with NaN in the 'areas_of_improvement' column
df = df.dropna(subset=['areas_of_improvement'])

# Extract the text data from the areas_of_improvement column
all_responses = ' '.join(df['areas_of_improvement'].astype(str).tolist())

# Generate the word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_responses)

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
```



![png](output_17_0.png)

# THEMATIC ANALYSIS

import pandas as pd


# Define a function to categorize each entry into themes
def categorize_entry(entry):
    themes = {
        "Infrastructure Upgrades": ["infrastructure", "leaks", "repair", "upgrade", "rehabilitation"],
        "Water Conservation and Efficiency": ["water-saving", "inefficient use", "consumption", "efficiency"],
        "Wastewater Management": ["wastewater treatment", "purification", "effluent"],
        "Water Governance and Policy": ["governance", "regulations", "accountability", "community participation"],
        "Resource Management": ["wetland management", "underground water", "new dam", "water bodies"],
        "Technological Integration": ["geospatial", "data collection"]
    }

    # Categorize the entry based on keywords
    entry_themes = []
    for theme, keywords in themes.items():
        if any(keyword in entry.lower() for keyword in keywords):
            entry_themes.append(theme)
    return entry_themes


# Apply the categorization function to each entry
df['themes'] = df['areas_of_improvement'].apply(categorize_entry)

# Count occurrences of each theme
theme_counts = {}
for themes_list in df['themes']:
    for theme in themes_list:
        if theme in theme_counts:
            theme_counts[theme] += 1
        else:
            theme_counts[theme] = 1

# Display the theme counts
print("Theme Counts:\n", theme_counts)

# Summarize entries by theme
for theme in theme_counts.keys():
    print(f"\nTheme: {theme}")
    print(df[df['themes'].apply(lambda x: theme in x)]['areas_of_improvement'].tolist())
```

Theme
Counts:
{'Infrastructure Upgrades': 16, 'Technological Integration': 8, 'Water Conservation and Efficiency': 9,
 'Resource Management': 35, 'Wastewater Management': 22, 'Water Governance and Policy': 2}

# THEME COUNTS VISUALIZATION

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# 1. Bar Chart of Theme Counts
theme_counts = {
    'Technological Integration': 7,
    'Water Conservation and Efficiency': 7,
    'Resource Management': 28,
    'Wastewater Management': 21,
    'Infrastructure Upgrades': 7
}

# Bar Chart of Theme Counts
plt.figure(figsize=(10, 6))
sns.barplot(x=list(theme_counts.keys()), y=list(theme_counts.values()), palette="viridis")
plt.title("Theme Counts")
plt.xlabel("Themes")
plt.ylabel("Count")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

plt.tight_layout()
plt.show()

sns.barplot(x=list(theme_counts.keys()), y=list(theme_counts.values()), palette="viridis")

![png](output_19_1.png)

< Figure size 640x480 with 0 Axes >
