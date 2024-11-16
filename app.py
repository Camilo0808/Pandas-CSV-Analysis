# app.py
from flask import Flask, request, jsonify
import pandas as pd
import io
from flask_talisman import Talisman

app = Flask(__name__)
Talisman(app, content_security_policy=None)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    if not file.filename.endswith('.csv'):
        return jsonify({"error": "Invalid file format. Only CSV files are allowed."}), 400

    try:
        content = file.read()
        df = pd.read_csv(io.BytesIO(content))

        response = {
            "columns": list(df.columns),
            "row_count": len(df),
            "column_summary": df.describe(include='all').to_dict()
        }

        return jsonify(response)
    except Exception as e:
        return jsonify({"error": f"Error processing file: {str(e)}"}), 500

@app.route('/column-stats', methods=['POST'])
def column_stats():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    column_name = request.form.get('column_name')

    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    if not file.filename.endswith('.csv'):
        return jsonify({"error": "Invalid file format. Only CSV files are allowed."}), 400

    if not column_name:
        return jsonify({"error": "No column name provided."}), 400

    try:
        content = file.read()
        df = pd.read_csv(io.BytesIO(content))

        if column_name not in df.columns:
            return jsonify({"error": f"Column '{column_name}' not found in the dataset."}), 400

        stats = {
            "mean": df[column_name].mean(),
            "median": df[column_name].median(),
            "std_dev": df[column_name].std(),
            "min": df[column_name].min(),
            "max": df[column_name].max(),
        }

        return jsonify(stats)
    except Exception as e:
        return jsonify({"error": f"Error processing file: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)