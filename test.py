import pandas as pd
df = pd.read_csv("Training_Raw_files_validated/Good_Raw/wafer_07012020_041011.csv")
#print(df.head())
for columns in df:
    #print(len(df[columns]))
    if (df[columns].isnull().sum() == len(df[columns])):
        print("Hi")