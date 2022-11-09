import pandas as pd 
import os
import glob
import pandas as pd


entries = os.listdir('/')
for entry in entries:
    print(entry)

all_files = glob.glob("/*.xlsx")
df = pd.concat((pd.read_excel(f) for f in all_files))
print("Done!")

df.to_excel('Final.xlsx', index=True, header=True)

print("Done!")