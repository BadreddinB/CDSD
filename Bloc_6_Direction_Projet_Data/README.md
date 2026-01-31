🌤️ ClimaSense — Short-term Climate Analysis & J+1 Forecasting

ClimaSense is a data science project focused on climate analysis of 20 French cities in 2022 and the development of a short-term temperature forecasting model (J+1) designed for operational decision support (e.g., road maintenance, frost prevention).

The project combines:

- Ingestion data with OpenMeteo

- Exploratory climate analysis (EDA),

- Detection of extreme weather events based on Météo France thresholds,

- A reproducible machine learning pipeline,

- An interactive Streamlit dashboard for decision-makers.

Main Problematic:

- Which elements characterize the climatic differences between French cities in 2022, and how can short-term variations (J+1) be anticipated for operational decision-making?

Sub-questions:

- How do temperatures and precipitation evolve throughout 2022?

- What climatic differences can be observed between cities?

- Which days can be considered meteorologically extreme?

- To what extent can these variations be predicted at J+1?

Project structure :

ClimaSense/
│
├── data/
│   ├── raw/            # Data collected from Open-Meteo API
│   ├── processed/      # Cleaned and engineered dataset
│   └── predictions/    # Model predictions (J+1)
│
├── models/             # One trained model per city (.pkl)
│
├── notebooks/
│   ├── 01_ingestion.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_model.ipynb
│   └── 04_streamlit.ipynb
│
├── streamlit_app/
│   └── app.py          # Streamlit dashboard
│
├── outputs/            # Generated figures
├── requirements.txt
└── README.md

Methodology Overview :

- Data source: Open-Meteo Archive API

- Period: January 1 – December 31, 2022

- Cities: 20 French cities representing different climate zones

Features:

- Lag variables (J-1 temperatures),

- Cyclical seasonal encoding (sin/cos),

Validation strategy:

- Time-based split (train: Jan–Sep, test: Oct–Dec),

- TimeSeriesSplit cross-validation,

Models compared:

- Linear Regression ✅ (selected),

- Polynomial Regression,

- Ridge Regression,

Evaluation metric: MAE (°C)

Key Results

- National MAE (J+1): ≈ 2.5°C

- Better predictability in Mediterranean climates (MAE < 2°C)

- More variability and prediction difficulty in continental/mountain climates

- Linear regression outperformed more complex models due to better generalization

Streamlit Decision Dashboard

The Streamlit app provides:

- City selection,

- Date filtering,

- Key performance indicators (MAE, accuracy ±2°C, frost-risk days),

- J+1 temperature forecast with operational recommendation,

- Historical prediction vs actual visualization,

- National comparison across cities.

How to Run the Project

Install dependencies :

pip install -r requirements.txt

Run notebooks in order :


