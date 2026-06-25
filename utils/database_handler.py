import os
from supabase import create_client, Client
from dotenv import load_dotenv
load_dotenv()
class DatabaseHandler():
  db: Client = create_client(
    supabase_key = os.environ.get("SUPABASE_KEY"),
    supabase_url = os.environ.get("SUPABASE_URL")
  )
  def get_data(self,table,query):
    response = self.db.table(table).select(query).execute()
    return response.data
  
  def insert_data(self, table, query):
    self.db.table(table).insert(query).execute()
