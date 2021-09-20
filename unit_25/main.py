# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data)
# print(type(data))
# print(data["day"])
# print(data["temp"])

data_dic = data.to_dict()
print(data_dic)

temp_list = data["temp"].to_list()
print(temp_list)

print(data["temp"].mean())
print(data["temp"].max())

# Get data in columns.

print(data["condition"])
print(data.condition)

print("# Get data in row.")
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])


print("(0°C × 9/5) + 32 = 32°F")
monday = data[data.day == "Monday"]
feh = int(monday.temp) * (9 / 5) + 32
print(feh)
