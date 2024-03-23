from flask import Flask, Response, render_template, request
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']

    if file.filename == '':
        return render_template('406.html')
    
    if file:
        filename = file.filename
        if filename.endswith('.csv') or filename.endswith('.xls') or filename.endswith('.xlsx'):
            df = pd.read_excel(file) if filename.endswith('.xls') or filename.endswith('.xlsx') else pd.read_csv(file)
            # Here you can perform operations on the DataFrame (df) as needed
            
            html_table = df.to_html(classes="table", escape=False)
            return render_template('dis.html', dataframe=html_table)#return df.to_html()  # For demonstration purpose, returning HTML representation of DataFrame
        else:
            return render_template('406.html')

if __name__ == '__main__':
    app.run(debug=True)
