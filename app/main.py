import mysql.connector
from flask import Flask

app = Flask(__name__)

DB_HOST = "db"
DB_PORT = 3306
DB_NAME = "test"
DB_TABLE = "TestTable"
DB_USER = "root"
DB_PASS = "secret"

@app.route("/data")
def get_data():
    try:
        db = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME
        )

        cursor = db.cursor()
        cursor.execute("SELECT * FROM TestTable")
        results = cursor.fetchall()

        json = {}
        for r in results:
            json[r[0]] = r[1]
        return json
    except:
        print("FAILED TO CONNECT")
        return {}

@app.route('/')
def home():
    return '''
    <html>
        <head>
            <title>Test</title>
        </head>
        <style>
            table, tr, th {
                border: 1px solid black;
            }
        </style>
        <script
  src="https://code.jquery.com/jquery-3.6.0.min.js"
  integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4="
  crossorigin="anonymous"></script>
        <script>
            $.getJSON("/data", function(data) {
                table = document.getElementById("data-table");
                for (var key in data) {
                    row = document.createElement("tr");
                    col1 = document.createElement("td");
                    col1.innerHTML = key;
                    col2 = document.createElement("td");
                    col2.innerHTML = data[key];
                    row.appendChild(col1);
                    row.appendChild(col2);
                    table.appendChild(row);
                }
            });
        </script>
        <body>
            <center>
                <h2>Testing Get Data</h2>
                <table id="data-table">
                    <tr><th>ID</th><th>Data</th></tr>
                </table>
            </center>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)