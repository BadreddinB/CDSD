# Uber Hot-Zones Prediction
## Unsupervised Demand Clustering for Operational Driver Positioning

## Business Problem

One of Uber’s key operational challenges is the geographical mismatch between available drivers and incoming ride requests.

When estimated waiting time exceeds 5 to 7 minutes, cancellation rates increase significantly, directly impacting:

Customer satisfaction

Platform efficiency

Driver revenue

Ride completion rate

The objective of this project is to leverage historical pickup data in order to:

✔ Identify geographically dense demand zones
✔ Provide data-driven positioning recommendations to drivers
✔ Reduce passenger waiting time through anticipatory supply allocation

## Analytical Objective

Using historical Uber pickup data from New York City (April 2014), the goal is to:

Detect recurring spatial demand patterns and define operational hot-zones where drivers should position themselves depending on the day of the week.

This is formulated as an unsupervised spatial clustering problem based on:

Pickup latitude

Pickup longitude

Temporal demand patterns

## Analytical Architecture

The predictive workflow follows a structured machine learning pipeline:

Raw Uber Pickup Data
        ↓
Temporal Feature Engineering
(hour / week_day extraction)
        ↓
Data Filtering by Time Slot
        ↓
Feature Scaling
(StandardScaler)
        ↓
Spatial Clustering
(KMeans / DBSCAN comparison)
        ↓
Cluster Evaluation
(Silhouette / DB Index / CH Index)
        ↓
Hot-Zone Identification
(cluster centroids)
        ↓
Driver Positioning Recommendation

Each model is trained independently for:

-> Each day of the week
-> All hourly demand observations

This allows operational recommendations to adapt dynamically to recurring demand patterns.

## Dataset

| Property        | Value                               |
| --------------- | ----------------------------------- |
| Source          | Uber NYC Pickups                    |
| Period          | April 2014                          |
| Volume          | ~564,000 pickups                    |
| Sample Used     | 10,000 observations                 |
| Sampling Method | Random sampling (`random_state=42`) |


Each record contains:

- Pickup date and time

- Latitude & longitude

- Dispatch base identifier

## Feature Engineering

Temporal variables were extracted from the pickup timestamp:

- hour → Hour of the day

- week_day → Day of the week

These engineered features enable:

- Time-specific demand filtering

- Model training per operational time slot

- Demand segmentation by recurring weekly patterns

## Model Comparison

Two clustering algorithms were evaluated:

KMeans

- Assigns each pickup to one of k clusters

- Covers 100% of observations

- Requires predefined number of clusters

DBSCAN

- Automatically detects dense spatial regions

- Identifies noise (isolated pickups)

- Requires eps and min_samples

### Model Evaluation (Monday — 6 PM)

| Metric                  | KMeans | DBSCAN |
| ----------------------- | ------ | ------ |
| Silhouette Score        | 0.41   | —      |
| Davies-Bouldin Index    | 0.47   | —      |
| Calinski-Harabasz Index | 121.20 | —      |
| Operational Coverage    | 100%   | 22%    |

DBSCAN detected only one valid cluster and classified 78% of pickups as noise, preventing actionable operational recommendations.

-> KMeans was selected as the final model

### Operational Hot-Zones

A KMeans model with k = 8 clusters was trained independently for each day of the week.

Cluster centroids represent:

- Recommended positioning zones for drivers
- Recurring demand hotspots

Demand patterns vary significantly:

- Weekdays → High concentration in Midtown & Lower Manhattan

- Weekends → More spatially distributed demand

## Reproducibility

### Clone the repository

git clone https://github.com/BadreddinB/CDSD.git
cd CDSD/Bloc_3_IA_Predictive_Structuree/Uber_Pickups

### Install dependencies

pip install -r requirements.txt

### Dataset location
Place the dataset in:

Uber_Pickups/data/uber-raw-data-apr14.csv

### Run the pipeline

uber.ipynb

## Project Structure

Uber_Pickups/
│
├── data/
│   └── uber-raw-data-apr14.csv
│
├── uber.ipynb
└── README.md

## Business Impct

By recommending dynamic positioning zones based on recurring demand patterns, Uber can:

- Reduce passenger waiting time

- Improve ride completion rates

- Increase driver utilization

- Optimize supply-demand matching

This predictive approach enables proactive driver positioning to maintain waiting times below the critical 5–7 minute threshold.

