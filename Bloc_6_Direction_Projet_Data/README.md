# 🌤️ ClimaSense — J+1 Temperature Forecast Dashboard

## ClimaSense is a data science project focused on the analysis of climatic differences between 20 French cities in 2022 and the development of a short-term temperature forecasting system (J+1) for operational decision support.

## The project combines:

- Ingestion data with OpenMeteo

- Exploratory climate analysis (EDA),

- Detection of extreme weather events based on Météo France thresholds,

- A machine learning time series forecasting,

- An interactive Streamlit dashboard for decision-makers.

## Main Problematic:

- Which elements characterize the climatic differences between French cities in 2022, and how can short-term variations (J+1) be anticipated for operational decision-making?

### Sub-questions:

- How do temperatures and precipitation evolve throughout 2022?

- What climatic differences can be observed between French cities?

- Which days can be considered meteorologically extreme according to Météo France thresholds?

- To what extent can these variations be predicted at J+1?

## Project structure :

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

## Methodology Overview :

- Data source: Open-Meteo Archive API

- Period: January 1 – December 31, 2022

- Cities: 20 French cities representing different climate zones

### Features:

- Lag variables (J-1 temperatures),

- Cyclical seasonal encoding (sin/cos),

### Validation strategy:

- Time-based split (train: Jan–Sep, test: Oct–Dec),

- TimeSeriesSplit cross-validation,

### Models compared:

- Linear Regression ✅ (selected),

- Polynomial Regression,

- Ridge Regression,

Evaluation metric: MAE (°C)

### Key Results:

- National MAE (J+1): ≈ 2.5°C

- Better predictability in Mediterranean climates (MAE < 2°C)

- More variability and prediction difficulty in continental/mountain climates

- Linear regression outperformed more complex models due to better generalization

## Streamlit Decision Dashboard

The Streamlit app provides:

- City selection,

- Date filtering,

- Key performance indicators (MAE, accuracy ±2°C, frost-risk days),

- J+1 temperature forecast with operational recommendation,

- Historical prediction vs actual visualization,

- National comparison across cities.

## Reproductibility :

git clone https://github.com/BadreddinB/CDSD.git
cd CDSD/Bloc_6_Direction_Projet_Data/ClimaSense

### Create a virtual environment :

python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

### Install dependencies

pip install -r requirements.txt

### Run notebooks in order :

jupyter notebook notebooks/01_ingestion.ipynb
jupyter notebook notebooks/02_eda.ipynb
jupyter notebook notebooks/03_model.ipynb

### Launch the Streamlit dashboard :

streamlit run streamlit_app/app.py

Then open your browser at:

http://localhost:8501

## Tech Stack :

- Python, Pandas, NumPy

- Scikit-learn

- Matplotlib, Seaborn

- Streamlit

- Open-Meteo API
