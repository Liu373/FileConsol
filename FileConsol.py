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
      
      if re.match("xxx_xxx_2018(\d+).csv", csv) or re.match("xxx_xxx_2019(\d+).csv", csv):
        File_Locatiion = path + '\\' + csv
        Year = re.search("xxx_xxx_(\d+).csv", csv).group(1)
        
        F_M = pd.read_csv(File_Location)
        
        x
        x
        x
        x
        x
        
        FileConsol = FileConsol.append(F_M)
        
      FileConsol.fillna(0, inplace=True)
      FileConsol.to_csv(save_location)
      
      print("It's done")
      



if __name__ == '__main__':
  
  path = r'C:\xx\xx\xx'
  save_location = r'C:\xx\xx\xxxx.csv'
  
  File_Loop = File_Loop(path = path, save_location = save_location)
  
  start_time = time.time()
  File_Loop._processing()
  print('Time: ' + time.strftime("%H:%M:%S", time.gmtime(time.time() - start_time)))
























