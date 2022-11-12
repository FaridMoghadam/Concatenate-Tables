import os
import glob
import pandas as pd

class Preprocess:
   #-- This section is for Splitting Excel files and merging them all
   def Concatenate_Table(self):
      try:
        all_files = glob.glob("*.xlsx")
        df = pd.concat((pd.read_excel(f) for f in all_files))
        return df
      except:
        print("I cannot Concatenate!")

   #-- Create a new file that contains all Excel data 
   def create_file(self): 
      try:
         df = Preprocess().Concatenate_Table()
         df.to_excel('Final.xlsx', index=True, header=True)
      except:
         print("I cannot create New File!")
      else:
         print("Created New File Done.")

if __name__ == '__main__':
    Preprocess().create_file()
