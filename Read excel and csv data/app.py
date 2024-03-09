import csv

from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/csv')
def index():
    # Read data from CSV file
    rows = []
    with open('data.csv', 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            rows.append(row)

    # Render HTML template with data
    return render_template('index.html', rows=rows)

@app.route('/excel')
def excel():
    # Read data from Excel file
    df = pd.read_excel('dataa.xlsx')

    # Convert DataFrame to list of lists
    rows = df.values.tolist()

    # Render HTML template with data
    return render_template('excel.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
