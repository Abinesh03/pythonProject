#print("welcome")
import json

# open the file
with open('employee.json') as f:
   data = json.load(f)
   print(data)

#data = json.load('employee.json')
#print(data)



