# Uber Hot-Zones Recommendation System

## Unsupervised Spatial Clustering for Operational Driver Positioning

## Business Context

One of Uber’s main operational challenges is the geographical mismatch between:

- available drivers

- incoming ride requests

When passenger waiting time exceeds 5 to 7 minutes, the probability of ride cancellation increases significantly, negatively impacting:

- customer satisfaction

- platform efficiency

- driver utilization

- ride completion rate

The objective of this project is therefore to identify geographical areas where drivers should position themselves in anticipation of demand, depending on the day of the week in New York City.

## Project Objective

Using historical Uber pickup data, this analysis aims to:

- detect recurring spatial demand patterns

- segment pickup locations into operational demand zones

- recommend positioning areas for drivers based on temporal demand patterns

This problem is formulated as an unsupervised spatial clustering task, where pickup latitude and longitude are used to infer geographical demand concentration.

## Dataset

The dataset contains historical Uber pickup records in New York City for April 2014 (~564,000 observations).

Each record includes:

- pickup timestamp

- pickup latitude

- pickup longitude

- dispatch base identifier

To reduce computational cost during clustering tuning, a random sample of 10,000 observations was used (random_state = 42) without significantly altering spatial demand distribution.

## Modeling Approach

### Temporal Feature Engineering

In order to account for recurring demand patterns, two temporal variables were extracted from the pickup timestamp:

- hour → hour of the day

- week_day → day of the week

These engineered features allow the training of time-specific models (e.g., Monday at 6PM), reflecting real operational demand fluctuations.

### Algorithm Benchmark — KMeans vs DBSCAN

Two clustering algorithms were evaluated to segment pickup locations into geographical demand zones:

KMeans

- assigns each pickup to a predefined cluster

- guarantees full spatial assignment

DBSCAN

- detects dense spatial regions

- classifies isolated pickups as noise

Clustering performance was evaluated using internal validation metrics:

- Silhouette Score

- Davies–Bouldin Index

- Calinski–Harabasz Index

as well as an additional operational metric:

-> Actionable Coverage Rate (ACR)
representing the proportion of pickups assigned to a usable cluster.

### Operational Model Selection (Monday — 6PM)

| Metric                   | KMeans | DBSCAN |
| ------------------------ | ------ | ------ |
| Silhouette Score         | 0.41   | —      |
| Davies-Bouldin Index     | 0.47   | —      |
| Calinski-Harabasz Index  | 121.20 | —      |
| Actionable Coverage Rate | 100%   | 22%    |

DBSCAN classified nearly 78% of pickups as noise, preventing their translation into actionable positioning recommendations.

Although capable of detecting dense areas, the algorithm failed to provide sufficient spatial segmentation for operational deployment.

KMeans, on the other hand, ensured full spatial assignment and usable demand zones.

-> KMeans was therefore selected as the final model based on operational usability rather than clustering performance alone.

### Weekday-Specific Hot-Zones Detection

A KMeans model (k = 8) was trained independently for each day of the week.

Cluster centroids represent:

- recurring pickup demand zones

- recommended positioning areas for drivers

Demand patterns vary significantly:

- Weekdays → strong concentration in Midtown and Lower Manhattan

- Other days → more spatially distributed ride requests

This suggests that optimal driver positioning strategies should dynamically adapt depending on the day of the week.

## Business Impact

By recommending positioning zones based on recurring spatial demand patterns, Uber can:

- reduce passenger waiting time

- improve driver utilization

- increase ride completion rates

- decrease cancellation probability

- optimize supply-demand matching

This approach supports proactive fleet allocation and helps maintain waiting time below the critical 5–7 minute threshold.

## Repository Structure

### Uber_Pickups/
│
├── data/
│   └── uber-raw-data-apr14.csv
│
├── uber.ipynb
└── README.md

## Reproducibility

### Clone the repository:

git clone https://github.com/BadreddinB/CDSD.git

### Navigate to the project folder:

cd CDSD/Bloc_3_IA_Predictive_Structuree/Uber_Pickups

### Place the dataset in:

Uber_Pickups/data/uber-raw-data-apr14.csv

### Run the notebook:

jupyter notebook uber.ipynb



