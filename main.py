from flask import Flask, render_template, request
from utils.file_parser import FileParser
app = Flask(__name__)
new_file = FileParser("./data.csv")

@app.route("/")
def landing():
  parsed = new_file.read_csv()
  page = request.args.get('page', 1, type=int)
  per_page = 20
  start = (page-1) * per_page
  end = start + per_page
  return render_template("index.html", 
                         columns=parsed.columns.tolist(), 
                         rows=parsed.values.tolist()[start:end], 
                         current_page=page)
