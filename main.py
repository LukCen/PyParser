from flask import Flask, render_template, request
from utils.file_parser import FileParser
app = Flask(__name__)

def filtered_data(data_from_file, type, index):
  if type=="column":
    return data_from_file[index]

@app.route("/", methods=["GET","POST"])
def landing():
  new_file = request.files.get('user_file')
  page = request.args.get('page', 1, type=int)
  per_page = 20
  start = (page-1) * per_page
  end = start + per_page
  
  if new_file is not None:
    parsed = FileParser(new_file).read_csv()
    # clean up header columns and capitalize them
    formatted_columns = [a.capitalize().replace("_"," ") for a in parsed.columns]
    dataset_for_filters = parsed.to_dict(orient="records")
    return render_template("index.html", 
                          columns=formatted_columns, 
                          rows=parsed.to_numpy().tolist(), 
                          current_page=page,
                          for_filters=dataset_for_filters)
  else: return render_template("index.html", columns=None, rows=None, current_page=page)


@app.route("/filter-column", methods=["GET","POST"])
def filtered():
  return f"<span>{ request.form.get('filter_column')}</span>"
 
