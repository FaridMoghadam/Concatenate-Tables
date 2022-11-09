import pandas as pd 
import os
import glob
import pandas as pd

class Preprocess:
   def listdir_labels(self):
      #-- This section is for identifying all the files in this folder.
      try:
        entries = os.listdir()
      except:
        print("Something went wrong !")
      else:
        print("I found some files.")
        Preprocess().create_Table()

   def Concatenate_Table(self):
      #-- Splitting Excel files and merging them all
      try:
        all_files = glob.glob("*.xlsx")
        df = pd.concat((pd.read_excel(f) for f in all_files))
        return df
      except:
        print("I cannot Concatenate !")
      
   def create_Table(self): 
      #-- Create a new file that contains all Excel data
      try:
         df = Preprocess().Concatenate_Table()
         df.to_excel('Final.xlsx', index=True, header=True)
      except:
         print("I cannot create New File !")
      else:
         print("Created New File Done.")

if __name__ == '__main__':
    Preprocess().listdir_labels()
