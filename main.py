from flask import Flask, render_template
from utils.file_parser import FileParser
app = Flask(__name__)
new_file = FileParser("./data.csv")

@app.route("/")
def landing():
  parsed = new_file.read_csv()
  return render_template("index.html", columns=parsed.columns.tolist(), rows=parsed.values.tolist())
