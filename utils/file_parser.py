import pandas as pd
class FileParser():
  def __init__(self,file):
    self.file = file

  def read_csv(self):
    contents = pd.read_csv(self.file)
    df = pd.DataFrame(contents)
    return df

  def get_column_values(self, column_name):
    if column_name in self.file.columns:
      return self.file[column_name]
    return []
