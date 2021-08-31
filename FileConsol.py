import pandas as pd
import os
import re
import time


class File_Loop:
  
  def __init__(self, path, save_location):
    self.path = path
    self.save_location = save_location
  
  
  def _processing(self):
    FileConsol = pd.DataFrame()
    
    for csv in os.listdir(self.path):
      
      if re.match("xxx_xxx_



























