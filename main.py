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
# data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# data["temp"].to_list()
# print(len(data["temp"].to_list()))

# average_temp = sum(data["temp"].to_list()) / len(data["temp"].to_list())
# print(average_temp)

# #OR 

# print(data["temp"].mean())

# max_temp = data["temp"].max()
# print(max_temp)

# #Get data in columns
# print(data["condition"])
# print(data.condition)

# #Get data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)

# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# #CREATE A DATA FRAME FROM SCRATCH
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")    


data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)    

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

print(data_dict)

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")