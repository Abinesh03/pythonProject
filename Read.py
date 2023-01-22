import csv


#Print the particular column in a CSV file
with open ('Read file.csv','r') as file:
    sports = csv.reader(file)
    for column in sports:
        print(column[0])

print("compare")

#Open a CSV file and print all values
'''
file = open('Read file.csv')
for line in file:
   print(line)
'''

print("qork")
