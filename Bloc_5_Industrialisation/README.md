# Getaround — Rental Delay Analysis & Pricing Optimization

## Business Context

Getaround is a peer-to-peer car rental platform where vehicles are frequently booked for consecutive rentals.

Two key operational challenges arise from this usage pattern:

### Rental Scheduling Reliability

Late vehicle returns may directly impact the next scheduled driver, generating:

- waiting time

- booking cancellations

- customer dissatisfaction

Introducing a minimum delay between consecutive rentals could improve operational reliability —
but may also reduce vehicle availability and therefore owner revenue.

### Pricing Decision Support

Vehicle owners must manually define their daily rental price.

Suboptimal pricing may result in:

- reduced booking probability

- revenue loss

- non-competitive listings

Automating pricing recommendations through a predictive model would allow the platform to assist owners in setting market-aligned prices at scale.

## Project Objective

This project aims to:

- quantify operational conflicts caused by late checkouts

- simulate the impact of introducing a minimum delay between rentals

- build a machine learning model capable of predicting optimal daily rental prices

- deploy this model through a REST API

- expose business insights through an interactive dashboard

## Part 1 — Rental Delay Analysis (Notebook: 01_getaround_delay_analysis.ipynb)

### Data Preparation

The analysis focuses exclusively on completed rentals.

Missing checkout delays were replaced by 0 minutes in order to reflect operationally on-time returns.

### Exploratory Findings

- Late checkout rate: ~52% of completed rentals

- Consecutive rental exposure: ~9% of bookings

- Conflict rate (consecutive rentals only): ~16.75%

This indicates that:

-> Late returns are frequent
-> Nearly 1 in 6 tightly scheduled rentals results in an operational conflict

## Minimum Delay Simulation

| Buffer  | Conflicts Resolved | Bookings Affected |
| ------- | ------------------ | ----------------- |
| 30 min  | 66.6%              | 15.1%             |
| 60 min  | 78.2%              | 22.2%             |
| 120 min | 88.5%              | 36.7%             |

Even relatively short buffers significantly reduce scheduling conflicts, while larger thresholds may negatively impact vehicle availability.

### Connect vs Mobile Rentals

Conflict rate by check-in type:

- Mobile → ~20%

- Connect → ~12%

Applying a delay feature exclusively to Connect vehicles would therefore fail to address the majority of operational issues.

### Product Recommendation

Introducing a 30 to 60-minute minimum delay across all rentals appears to provide the best trade-off between:

- customer experience

- operational reliability

- owner revenue

## Part 2 — Pricing Optimization Model (Notebook: 02_getaround_pricing_model.ipynb)

### Modeling Objective

Predict the optimal rental price per day based on vehicle characteristics in order to:

- assist owners in pricing their listings

- increase listing competitiveness

- support automated pricing recommendations

### Modeling Pipeline

Preprocessing and model training are combined into a single pipeline to ensure consistent transformations between:

- training environment

- production API

#### Two models were evaluated:

- Model	MAE
- Linear Regression	13.06 €
- HistGradientBoostingRegressor	11.57 €

The gradient boosting model demonstrated better performance by capturing non-linear relationships between vehicle characteristics and rental price.

-> It was therefore selected for deployment.

### Experiment Tracking

Model training is tracked using MLflow:

- performance metric logging (MAE)

- pipeline versioning

- artifact storage

The final trained pipeline is serialized using joblib and exported for production use by the prediction API.

## Industrialization

### Project Architecture

Bloc_5_Industrialisation/
│
├── data/
├── notebooks/
│   ├── 01_getaround_delay_analysis.ipynb
│   └── 02_getaround_pricing_model.ipynb
│
├── dashboard/
│   └── app.py
│
├── api/
│   ├── fastapi_app.py
│   ├── schemas.py
│   └── model/
│       └── model.joblib
│
├── mlruns/
├── Dockerfile
├── requirements.txt
└── README.md


### API — FastAPI

The pricing model is served through a REST API that:

- accepts vehicle characteristics as input

- applies preprocessing and prediction pipeline

- returns a recommended rental price

### Dashboard — Streamlit

An interactive dashboard enables the Product Team to:

- explore delay analysis findings

- simulate minimum delay thresholds

- visualize conflict reduction vs booking impact

### Deployment

The full application is containerized using Docker and deployed on Hugging Face Spaces.

-> Live Application:
### https://huggingface.co/spaces/BadreddinB/getaround-analysis

## Business Impact

This industrialized pipeline enables Getaround to:

- reduce scheduling conflicts caused by late returns

- improve customer experience

- maintain operational reliability

- provide automated pricing recommendations

- support data-driven product decisions




