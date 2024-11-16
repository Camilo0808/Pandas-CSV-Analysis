# Data Insights API with Pandas

This project is a simple FastAPI application that leverages Pandas for data analysis. Users can upload CSV files, and the API will provide analytics such as column statistics and dataset summaries.

---

## Features
- Upload CSV files for analysis.
- Get a list of columns, row count, and descriptive statistics for the dataset.
- Retrieve specific statistics (mean, median, standard deviation, min, max) for any column.

---

## Requirements
- Python 3.9+
- Pandas
- FastAPI
- Uvicorn

---

## Getting Started

### 1. Clone the repository:
```bash
git clone 
cd Pandas-CSV-Analysis
```

### 2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 4. Run the application:
```bash
uvicorn main:app --reload
```

### 5. Access the API:
- Open your browser and navigate to `http://127.0.0.1:8000/docs` for the interactive Swagger UI.

---

## Endpoints

### POST `/upload`
**Description:** Upload a CSV file and get an overview of the dataset.

#### Response
```json
{
  "columns": ["Column1", "Column2", "Column3"],
  "row_count": 100,
  "column_summary": {
    "Column1": {
      "count": 100,
      "mean": 50.5,
      "std": 29.011,
      ...
    },
    ...
  }
}
```

### GET `/column-stats`
**Description:** Get statistics for a specific column in the uploaded CSV.

#### Query Parameters:
- `file`: CSV file to upload.
- `column_name`: Name of the column to analyze.

#### Response
```json
{
  "mean": 50.5,
  "median": 50.0,
  "std_dev": 29.011,
  "min": 1.0,
  "max": 100.0
}
```

---

## Project Structure
```
.
├── app.py
├── requirements.txt
└── README.md
```

---

## Requirements.txt
```
fastapi==0.98.0
uvicorn==0.22.0
pandas==2.1.1
```