from flask import Flask, render_template, request
from utils.file_parser import FileParser
from utils.database_handler import DatabaseHandler
from api.register_user import register_user
import json

app = Flask(__name__)

pyparse_users = DatabaseHandler()

with open('paths.json', "r") as f:
  paths = json.load(f)

# global variable injection
@app.context_processor
def global_navbar():
  return dict(navbar=paths)

def filtered_data(data_from_file, type, index):
  if type=="column":
    return data_from_file[index]

# landing page
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
 
@app.route("/register", methods=["GET","POST"])
def register():
  if request.method == "POST":
    payload = register_user()
    print(payload)
    pyparse_users.insert_data('registered_users',{"username": payload["username"], "password_hash":payload["password_hash"], "email":payload["email"],"blob_folder":f"/{payload["username"]}"})
    return render_template("register.html", temp_data = payload)
  return render_template("register.html")

@app.route("/db-test", methods=["GET","POST"])
def db_post():

  d = pyparse_users.get_data('registered_users', '*')
  return f"<span>{d}</span>"
