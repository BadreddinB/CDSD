# Tinder — Speed Dating Exploratory Data Analysis

## Business Context

Tinder's marketing team has observed a decrease in the number of matches on the platform.

In order to better understand what drives romantic interest between individuals during early interactions, a controlled speed dating experiment was conducted.

Participants met several potential partners and were asked whether they would like to see them again after each short interaction.

The objective of this analysis is to identify the factors associated with the decision to pursue a second date and provide actionable insights to improve Tinder’s matching strategy.

## Analytical Objective

This study evaluates how the following perceived partner characteristics influence the likelihood of agreeing to a second date:

Physical attractiveness

Shared interests

Perceived fun & emotional engagement

Intelligence & ambition

Sincerity

Demographic similarity (same race, meeting order)

## Decision-Making Perspective

The goal of this analysis is not only to explore participant preferences, but to identify which perceived partner characteristics significantly influence early romantic interest in a controlled experimental setting.

These insights are intended to support Tinder’s Product and Marketing teams in optimizing matching mechanisms and user profile features that may increase the likelihood of mutual matches on the platform.

By identifying the most influential compatibility signals in short interactions, this study contributes to a data-driven approach to improving user engagement and match formation.

## Dataset
Property	Value
Source	Speed Dating Experiment (Columbia University)
File	Speed+Dating+Data.csv
Shape	8,378 rows × 195 columns
Target variable	dec — Decision to pursue a second date (0 = No, 1 = Yes)
The dataset contains participant-level data including:

Demographics (age, gender, race, education, career)

Lifestyle indicators

Post-date partner ratings across perceived traits

Several columns contain more than 70% missing values.
These were excluded from the analysis to avoid biased results.

## Analytical Workflow

The analysis was conducted following a structured data analysis pipeline:

Data quality audit and handling of missing values

Construction of an analytical dataset containing key compatibility indicators

Exploratory population profiling

Bivariate analysis of partner traits and second-date decisions

Multivariate predictive modelling using Logistic Regression

Statistical inference to validate observed relationships

This workflow ensures that the insights produced are statistically grounded and reproducible for future product analysis.

## Analysis Structure

### Population Overview

Descriptive profiling of participants across key demographic dimensions:

Gender distribution

Age distribution

Field of study

Career intentions

Racial background

Overall match rate

### Bivariate Analysis

Exploration of the relationship between each partner attribute and the second-date decision.

Variable	Observed Effect
Attractiveness	Strong positive effect
Shared interests	Strong positive effect
Fun	Strong positive effect
Intelligence	Moderate positive effect
Ambition	Weak / no effect
Sincerity	Weak / no effect
Same race	Marginal effect
Meeting order	No effect

### Multivariate Analysis — Logistic Regression

A logistic regression model was trained on standardized features to assess the combined and independent impact of each variable on second-date decisions.

Variable	Coefficient	Interpretation
Attractiveness	+1.07	Strongest predictor
Shared interests	+0.58	Strong predictor
Fun	+0.52	Strong predictor
Intelligence	+0.04	Negligible
Same race	−0.01	Negligible
Meeting order	−0.05	Negligible
Sincerity	−0.20	Slight negative
Ambition	−0.30	Slight negative

### Inferential Analysis

Statistical tests were conducted to validate observed differences.

Test	Variable	p-value	Result
Welch t-test	Attractiveness	< 0.001	✅ Significant
Welch t-test	Shared interests	< 0.001	✅ Significant
Chi-square	Same race	0.009	✅ Significant (weak effect)
Welch t-test	Meeting order	0.161	❌ Not significant

## Key Findings

Perceived physical attractiveness is the strongest predictor of second-date decisions.

Shared interests and perceived fun are also highly influential.

Emotional compatibility appears more important than demographic similarity.

Meeting order does not significantly influence romantic interest.

Ambition and sincerity are difficult to assess during brief interactions.

## Business Recommendations for Tinder

These findings suggest that Tinder’s matching strategy could benefit from:

Prioritizing visual quality
Profile photos significantly impact match likelihood.

Interest-based matching
Surfacing shared hobbies and lifestyle compatibility signals could improve match rates.

Personality-driven profiles
Features that convey fun, humor, and engagement may foster more successful interactions.

## Tech Stack

Category	Tools
Language	Python 3
Data manipulation	pandas
Visualization	matplotlib, seaborn
Modelling	scikit-learn
Statistical testing	scipy

## Reproductibility

Bloc_2_Analyse_Exploratoire/
│
├── Tinder/
│   ├── data/
│   │   └── Speed+Dating+Data.csv
│   └── Tinder_analysis.ipynb
│
├── requirements.txt
└── README.md

### Clone the reposotory

git clone https://github.com/BadreddinB/Bloc_2_Analyse_Exploratoire.git
cd Bloc_2_Analyse_Exploratoire

### Install dependencies

pip install -r requirements.txt

### Dataset
Place the dataset in the following directory:

Tinder/data/Speed+Dating+Data.csv

### Run the analysis

Launch Jupyter Notebook and execute:

Tinder/Tinder_analysis.ipynb

All visualizations and statistical analyses will be generated automatically by running the notebook sequentially.




