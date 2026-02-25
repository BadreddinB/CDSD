# ============================
# BASE IMAGE
# ============================

FROM python:3.10-slim

# ============================
# WORKDIR
# ============================

WORKDIR /app

# ============================
# COPY FILES
# ============================

COPY . .

# ============================
# INSTALL DEPENDENCIES
# ============================

RUN pip install --upgrade pip
RUN pip install -r requirements-prod.txt

# ============================
# EXPOSE PORTS
# ============================

EXPOSE 8000
EXPOSE 8501

# ============================
# START API + DASHBOARD
# ============================

CMD uvicorn api.fastapi_app:app --host 0.0.0.0 --port 8000 & \
    streamlit run dashboard/app.py \
    --server.port 8501 \
    --server.address 0.0.0.0