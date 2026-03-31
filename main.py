#with open("weather_data.csv") as data_file:
#   data = data_file.readlines()
#   print(data)

#the above was done to put the data in the list but not very efficient way 

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     for row in data:
#         print(row)

#Here i used csv module to read the data and print it row by row. This is a more efficient way to handle CSV files in Python.But not the best yet, we can use pandas library to handle CSV files more efficiently and easily.
#After using csv everything was sepeerated as a single string, we can use pandas to handle the data in a more structured way.

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     Temperature = []
#     for row in data:
#         if row[1] != "temp":
#             Temperature.append(int(row[1]))
#     print(Temperature)

#Here i used csv module to read the data and print only the temperature column. I created an empty list called Temperature and then looped through each row in the data. If the second element of the row (which is the temperature) is not equal to "temp" (the header), I converted it to an integer and appended it to the Temperature list. Finally, I printed the Temperature list.
      
import pandas
data = pandas.read_csv("weather_data.csv")
print(data)
print(data["temp"])