import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")

# Display general summary statistics
summary_stats = data.describe()

# Create subplots with increased vertical space between the first two rows and increased horizontal space between the first two columns
fig, axs = plt.subplots(2, 2, figsize=(15, 15), gridspec_kw={'hspace': 0.5, 'wspace': 0.5})  

# Add Name and Student ID more to the top left corner
fig.text(0.02, 0.99, r'$\bf{Name:}$ Fawas Afsal' + '\n' + r'$\bf{Student\ ID:}$ 22080258', fontsize=12, va='top', ha='left')

# Add introductory text
intro_text = (
    "The dataset provides a basis for understanding the prevalence of sleep disorders among different age groups and occupations."
    " It could be used to analyze lifestyle factors, such as exercise frequency and its impact on sleep health, BMI categories, blood pressure, and heart rate etc."
)

# Add more space above the intro_text
fig.text(0.5, 0.94, intro_text, ha='center', fontsize=12, va='top', wrap=True)

# Plot 1: Age Distribution
sns.histplot(data['Age'], bins=20, kde=True, color='skyblue', ax=axs[0, 0])
axs[0, 0].set_title(r'$\bf{Age\ Distribution}$', color='red')  # Bold and red headline
axs[0, 0].set_xlabel('Age')
axs[0, 0].set_ylabel('Frequency')

# Add insight in a rounded box with light background color
insight_text_1 = (
    "Insights shown is a diverse age range, enabling the analysis of sleep health trends\n across different life stages. "
    "The age distribution is relatively even across different age groups.\n "
    "There is a peak in the early 50s, suggesting a concentration of individuals in this age range."
)

# Add insight as an annotation below the first graph
axs[0, 0].annotate(insight_text_1, xy=(0.5, -0.25), xycoords='axes fraction',
                   bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.5),
                   ha='center', fontsize=10, color='black')

# Plot 2: Sleep Duration Distribution by Occupation
sns.barplot(x='Sleep Duration', y='Occupation', data=data, palette='viridis', ax=axs[0, 1])
axs[0, 1].set_title(r'$\bf{Average\ Sleep\ Duration\ by\ Occupation}$', color='red')  # Bold and red headline
axs[0, 1].set_xlabel('Sleep Duration (hours)')
axs[0, 1].set_ylabel('Occupation')

# Add insight text below the second graph with a light background color
insight_text_2 = (
    "Occupation appears to influence sleep duration, highlighting the importance of considering\n work-related factors in sleep health interventions."
    " Nurses and doctors tend to have \nshorter sleep durations on average, possibly due to the demanding \nnature of their jobs. Engineers, on the other hand, exhibit a more consistent sleep duration."
)

# Add insight as an annotation below the second graph
axs[0, 1].annotate(insight_text_2, xy=(0.5, -0.25), xycoords='axes fraction',
                   bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.5),
                   ha='center', fontsize=10, color='black')

# Plot 3: BMI Category Distribution
data['BMI Category'].value_counts().plot.pie(autopct='%1.1f%%', colors=sns.color_palette('pastel'), ax=axs[1, 0])
axs[1, 0].set_title(r'$\bf{BMI\ Category\ Distribution}$', color='red')  # Bold and red headline
axs[1, 0].set_ylabel('')
axs[1, 0].legend(data['BMI Category'].value_counts().index, loc="upper left", bbox_to_anchor=(0.85, 1))

# Add insight text below the third graph with a light background color
insight_text_3 = (
    "The prevalence of individuals in the 'Overweight' category signals a potential area\n for health interventionsand awareness campaigns related to \nsleep health."
    " A significant portion falls into the 'Overweight' category."
)

# Add insight as an annotation below the third graph
axs[1, 0].annotate(insight_text_3, xy=(0.5, -0.25), xycoords='axes fraction',
                   bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.5),
                   ha='center', fontsize=10, color='black')

# Plot 4: Heart Rate Distribution by Sleep Disorder
sns.violinplot(x='Sleep Disorder', y='Heart Rate', data=data, palette='muted', ax=axs[1, 1])
axs[1, 1].set_title(r'$\bf{Heart\ Rate\ Distribution\ by\ Sleep\ Disorder}$', color='red')  # Bold and red headline
axs[1, 1].set_xlabel('Sleep Disorder')
axs[1, 1].set_ylabel('Heart Rate')

# Add insight text below the fourth graph with a light background color
insight_text_4 = (
    "The association between sleep disorders, particularly sleep apnea, and a wider \nrange of heart rates suggests a potential link between sleep health\n and cardiovascular well-being."
    " Individuals with sleep apnea exhibit a\n wider range of heart rates compared to those with no sleep disorders."
)

# Add insight as an annotation below the fourth graph
axs[1, 1].annotate(insight_text_4, xy=(0.5, -0.25), xycoords='axes fraction',
                   bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.5),
                   ha='center', fontsize=10, color='black')

# Add summary as text annotation
summary_text = (
    "\n\nIn summary, the dataset paints a nuanced picture of the interplay between age, occupation, sleep duration, BMI, "
    "and heart rate. These visualizations offer a holistic understanding of the factors influencing sleep health and lifestyle "
    "choices, setting the stage for more in-depth analyses and targeted interventions to improve overall well-being.\n\n"
)

fig.suptitle(r'$\bf{Sleep\ Health\ and\ Lifestyle}$', y=1.0, fontsize=16)  # Bold title
fig.text(0.5, 0.02, summary_text, ha='center', fontsize=12, va='top', wrap=True)

# Add more space below summary_text
fig.subplots_adjust(bottom=0.1)

# Save the plot as an image
plt.savefig("22080258.png", dpi=300)

# Display the plot
plt.show()

