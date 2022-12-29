import pandas as pd

# Load the xlsx file
excel_data = pd.read_excel('Sample.xlsx')
# Read the values of the file in the dataframe
data = pd.DataFrame(excel_data, columns=['User', 'Status', 'Mark'])
# Print the content
print("The content of the file is:\n", data)
