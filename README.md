# Financial Crisis Early-Warning Orchestrator (FCEWO)

An AI-driven real-time financial crisis early-warning system built with Streamlit, FastAPI, Supabase, Grafana, Prometheus, and Docker.

## 🏗️ Architecture

- **Frontend**: Streamlit web application for user interface
- **Backend**: FastAPI REST API for data processing and ML predictions
- **Database**: Supabase (PostgreSQL) for data storage
- **Monitoring**: Prometheus for metrics collection and Grafana for visualization
- **Containerization**: Docker Compose for orchestration

## 🚀 Features

- Real-time financial data analysis
- AI/ML-powered crisis risk prediction
- Early warning alerts system
- Market indicators monitoring
- Interactive dashboards
- Prometheus metrics collection
- Grafana visualization

## 📋 Prerequisites

- Docker and Docker Compose
- Supabase account and project
- Python 3.11+ (for local development)

## 🚀 Quick Start

### Easiest Way (All Platforms)

**Windows:**
```bash
run.bat
```

**Linux/Mac:**
```bash
chmod +x run.sh
./run.sh
```

This will:
1. Check your setup
2. Create `.env` if needed
3. Let you choose Docker or local development
4. Start the services

### Manual Setup

1. **Test your setup:**
   ```bash
   python test_setup.py
   ```

2. **Configure environment:**
   ```bash
   cp env.example .env
   # Edit .env with your Supabase credentials (optional)
   ```

3. **Start with Docker:**
   ```bash
   docker-compose up --build
   ```

4. **Or run locally:**
   ```bash
   python run_local.py
   ```

### Supabase Setup (Optional - for full features)

1. Create a Supabase project at [supabase.com](https://supabase.com)
2. Run `supabase/schema.sql` in the SQL Editor
3. Copy your Project URL and Anon Key to `.env`

**Note:** The system can run without Supabase, but with limited functionality (no persistent alerts/predictions).

See [QUICKSTART.md](QUICKSTART.md) for detailed instructions.

## 📖 API Documentation

Once the API is running, visit:
- Swagger UI: http://localhost:8001/docs (default, configurable via API_PORT)
- ReDoc: http://localhost:8001/redoc (default, configurable via API_PORT)

## 🔍 API Endpoints

### Financial Data
- `GET /api/v1/financial/symbols/{symbol}` - Get financial data for a symbol
- `GET /api/v1/financial/symbols/{symbol}/history` - Get historical data
- `GET /api/v1/financial/indicators` - Get market indicators

### Predictions
- `POST /api/v1/predictions/predict` - Generate risk predictions
- `GET /api/v1/predictions/predict/{symbol}` - Get latest prediction

### Alerts
- `GET /api/v1/alerts/` - Get alerts (with filters)
- `POST /api/v1/alerts/` - Create alert
- `PATCH /api/v1/alerts/{id}/acknowledge` - Acknowledge alert
- `GET /api/v1/alerts/stats` - Get alert statistics

## 🎯 Usage

### Frontend (Streamlit)

1. Navigate to http://localhost:8501
2. Enter stock symbols (comma-separated) in the sidebar
3. Select lookback period
4. View predictions, alerts, and market indicators

### Monitoring

- **Prometheus**: http://localhost:9091 (default, configurable via PROMETHEUS_PORT)
- **Grafana**: http://localhost:3001 (default, configurable via GRAFANA_PORT)
  - Default credentials: admin/admin
  - Prometheus datasource is pre-configured

## 🧪 Development

### Local Development (without Docker)

#### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

#### Frontend
```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

## 📊 ML Model

The early warning system uses:
- **Isolation Forest** for anomaly detection
- **Random Forest** for risk classification
- Technical indicators (RSI, MACD, volatility, drawdown)

Features extracted:
- Price movements and returns
- Volume trends
- Technical indicators
- Market volatility

## 🔐 Security Notes

- Update default Grafana credentials in production
- Configure proper RLS policies in Supabase
- Use environment variables for sensitive data
- Enable HTTPS in production

## 📝 License

MIT License

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Support

For issues and questions, please open an issue on GitHub.

