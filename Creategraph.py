import pandas as pd
#import matplotlip.pyplot as plt

#excel_data = "categorization.xlsx"

excel_data = pd.read_excel("categorization.xlsx")
#print(df.head())
data = pd.DataFrame(excel_data, columns=['mailcategory'])
#folders = df[["mailcategory"]]
#print(folders)
print("The content of the file is:\n", data)