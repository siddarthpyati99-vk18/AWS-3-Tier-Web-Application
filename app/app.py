from flask import Flask
import pymysql
import boto3
import json

app = Flask(__name__)

SECRET_NAME = "three-tier-db-credentials"
REGION = "us-east-1"
DB_HOST = "YOUR_RDS_ENDPOINT"
DB_NAME = "studentdb"


def get_secret():
    client = boto3.client("secretsmanager", region_name=REGION)
    response = client.get_secret_value(SecretId=SECRET_NAME)
    return json.loads(response["SecretString"])


def get_db_connection():
    secret = get_secret()
    return pymysql.connect(
        host=DB_HOST,
        user=secret["username"],
        password=secret["password"],
        database=DB_NAME,
        port=3306,
        cursorclass=pymysql.cursors.DictCursor,
    )


@app.route("/")
def home():
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM students")
            students = cursor.fetchall()
        connection.close()

        rows = ""
        for student in students:
            rows += (
                "<tr>"
                f"<td>{student['id']}</td>"
                f"<td>{student['name']}</td>"
                f"<td>{student['email']}</td>"
                f"<td>{student['course']}</td>"
                "</tr>"
            )

        return (
            "<!DOCTYPE html><html><head>"
            "<title>AWS 3-Tier Web Application</title>"
            "<style>"
            "body{font-family:Arial;background:#f4f7fb;padding:40px}"
            ".container{max-width:1100px;margin:auto;background:white;padding:40px;"
            "border-radius:15px;box-shadow:0 5px 25px rgba(0,0,0,.1)}"
            "h1{text-align:center;color:#1f3c5b}"
            ".status{text-align:center;color:green;font-weight:bold;margin-bottom:35px}"
            "table{width:100%;border-collapse:collapse}"
            "th{background:#243447;color:white;padding:15px;text-align:left}"
            "td{padding:14px;border-bottom:1px solid #ddd}"
            "</style></head><body><div class='container'>"
            "<h1>AWS 3-Tier Web Application</h1>"
            "<div class='status'>Application + RDS Connected</div>"
            "<h2>Students from Amazon RDS MySQL</h2>"
            "<table><tr><th>ID</th><th>Name</th><th>Email</th><th>Course</th></tr>"
            f"{rows}</table></div></body></html>"
        )
    except Exception as e:
        return f"<h1>Database Connection Error</h1><p>{e}</p>", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
