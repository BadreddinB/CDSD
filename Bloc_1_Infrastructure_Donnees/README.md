#  Kayak — Data Infrastructure Pipeline

## Business Context

Kayak is a travel search engine aiming to help users plan their next holidays based on reliable and objective data.

User research conducted by the Marketing team highlighted that:

- **70% of users** would like more trusted information about destinations before booking
- Users tend to **distrust content** if the data source is unknown

The Marketing team therefore wants to build a recommendation application able to suggest:
- The **best destinations** to travel to
- The **best hotels** available in those destinations

based on real-time environmental conditions such as weather forecast and accommodation quality.

---

## Business Objective

Kayak’s Marketing team aims to enhance user trust by recommending travel destinations based on objective environmental data rather than subjective content.

By combining short-term weather forecasts with accommodation quality indicators, the future application will be able to:

- Recommend destinations offering optimal climatic conditions
- Suggest highly rated accommodation options in those locations

In order to support this recommendation engine, a scalable data infrastructure must be implemented to collect, process and expose trusted travel-related data.

This pipeline therefore focuses on transforming external environmental and accommodation data into a structured, decision-ready dataset that can be leveraged by marketing teams for destination recommendation.

---

## Architecture Overview
External APIs & Web Data Lake ETL Pipeline Data Warehouse
┌─────────────────┐ ┌─────────┐ ┌────────────┐ ┌────────────┐
│ Nominatim (GPS) │──────▶│ │ │ │ │ │
│ Open-Meteo │──────▶│ AWS S3 │──────▶│ Transform │──────▶│ AWS RDS PG │
│ Booking.com │──────▶│ │ │ │ │ │
└─────────────────┘ └─────────┘ └────────────┘ └────────────┘


### Data Sources

| Source | Type | Data collected |
|---|---|---|
| Nominatim | REST API | GPS coordinates (lat/lon) |
| Open-Meteo | REST API | 7-day weather forecast |
| Booking.com | Web scraping (Selenium) | Hotel names, scores, URLs |

### Storage & Processing

- **AWS S3** — Data Lake for raw and enriched data
- **ETL Pipeline** — Cleaning, transformation, weather score engineering
- **AWS RDS (PostgreSQL)** — Data Warehouse for structured, queryable travel insights

---

## Pipeline Steps

### 1. GPS Coordinates Collection

Queries the Nominatim API to retrieve latitude and longitude for each of the 35 target cities in France.

### 2. Weather Data Collection

Calls the Open-Meteo API for a 7-day forecast per city, collecting:

- Daily maximum temperature
- Cumulative precipitation

### 3. Weather Attractiveness Score Engineering

A composite **Weather Score** is computed to rank destination attractiveness:
weather_score = avg_temp_7d - (rain_7d × 0.5)


Higher score = warmer and drier destination over the next 7 days.

### 4. Hotel Data Collection (Web Scraping)

Uses Selenium to scrape Booking.com for the top 5 destinations, collecting up to 20 hotels per city:

- Hotel name
- Review score
- Booking page URL
- Accommodation description

### 5. ETL — Data Transformation & Consolidation

- Cleans review scores (comma-to-dot normalization)
- Handles missing values
- Merges weather + GPS + hotel data into a single enriched dataset (`enriched_travel_data.csv`)

### 6. Data Lake Storage (AWS S3)

Uploads the enriched dataset to S3:
s3://kayak-data-lake-bucket/curated/enriched_travel_data.csv


### 7. Data Warehouse Loading (AWS RDS)

Extracts the file from S3 and loads it into a PostgreSQL table (`travel_data`) on AWS RDS for downstream querying.

---

## Decision-Support Dataset

The structured dataset stored in the Data Warehouse can be queried to:

- Identify the most attractive destinations
- Highlight top-rated hotels within those locations

---

## Business Impact

The structured dataset produced by this pipeline enables Kayak’s Marketing team to:

- Identify the most attractive destinations for short-term travel
- Highlight top-rated accommodation options in these locations
- Support destination recommendation based on objective criteria

This data-driven approach may improve user confidence in travel planning by relying on transparent and verifiable environmental information.

---

## Output

The final dataset combines:

| Column | Description |
|---|---|
| city_id / city_name | Destination identifier |
| latitude / longitude | GPS coordinates |
| rain_7d | Cumulative 7-day rainfall (mm) |
| avg_temp_7d | Average daily max temperature (°C) |
| weather_score | Climate attractiveness index |
| hotel_name | Hotel name |
| review_score | Guest review score (0–10) |
| booking_url | Direct Booking.com link |

---

## Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| Data manipulation | pandas |
| HTTP requests | requests |
| Web scraping | Selenium |
| Visualization | Plotly |
| Cloud storage | AWS S3 |
| Database | AWS RDS PostgreSQL |
| ORM | SQLAlchemy |
| Environment variables | python-dotenv |

---

## Setup & Configuration

### 1. Clone the repository

```bash
git clone https://github.com/BadreddinB/CDSD.git

# 2. Entrer dans le dossier du projet

cd CDSD

# 3. Aller dans le Bloc 1

cd cd Bloc_1_Infrastructure_Donnees

2. Install dependencies

pip install -r requirements.txt

3. Configure environment variables

Create a .env file:

AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_DEFAULT_REGION=your_region

RDS_HOST=your_rds_endpoint
RDS_PORT=5432
RDS_DB_NAME=your_db_name
RDS_USER=your_db_user
RDS_PASSWORD=your_db_password

4. Run the notebook
Kayak_Data-Infrastructure.ipynb

### Notes

Weather data is fetched in real time

Scores vary depending on execution date

Booking.com data is collected via web scraping

