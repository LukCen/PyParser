import pandas as pd
class FileParser():
  def __init__(self,file):
    self.file = file

  def read_csv(self):
    contents = pd.read_csv(self.file)
    df = pd.DataFrame(contents)
    return df
