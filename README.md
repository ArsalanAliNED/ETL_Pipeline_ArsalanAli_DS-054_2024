# 🚜 Agriculture ETL Pipeline

This project is an automated ETL (Extract, Transform, Load) pipeline built with Python to forecast crop yield using diverse data sources. It integrates Google Drive, Google Sheets, OpenWeatherMap API, MongoDB, and CI/CD workflows via GitHub Actions.

---

## 📦 Components

- `etl_pipeline.py`: Core ETL script that pulls, processes, and pushes data.
- `load_to_db.py`: Inserts pre-processed satellite data into MongoDB.
- `schedule.py`: Optional scheduler to run the pipeline daily.
- `.github/workflows/ci.yml`: CI/CD workflow file for automated testing and deployment.
- `test_etl.py`: Unit tests for the ETL outputs.
- `validate_schema.py`: Schema validation script to enforce data integrity.
- `schema.json`: Expected schema for final output validation.

---

## ⚙️ Setup Guide

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Add your configuration files**
   - Upload `db_config.json` to store your MongoDB URI:
     ```json
     {
       "mongo_uri": "your-mongodb-connection-string"
     }
     ```
   - Upload `sample_weather.json` for fallback weather data.

3. **Prepare Google Access**
   - Ensure your Google Sheet is shared with your authenticated Google account in Colab.
   - Place `crop_yield.csv` and config files in your Google Drive.

---

## 🚀 Running the Pipeline

```bash
python etl_pipeline.py
```

To schedule it:
```bash
python schedule.py
```

---

## 🧪 Testing and Validation

- **Unit Tests**: Run with `pytest test_etl.py`
- **Schema Check**: Run with `python validate_schema.py`

---

## 🔁 CI/CD (GitHub Actions)

On every push to `main`:
- Installs dependencies
- Runs unit tests
- Validates data schema
- Executes ETL pipeline if all tests pass

No manual deployments required.

