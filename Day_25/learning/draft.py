# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     data_list = list(data)
#     temperature = []
#     for row in data_list[1:]:
#         day_temperature = row[1]
#         temperature.append(int(day_temperature))
#
#     print(temperature)
#
import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data["temp"]))
data_dict = data.to_dict()
print(data_dict)
temp_list = data["temp"].to_list()
# sum_temp = sum(temp_list)
# average = (sum_temp/len(temp_list))
# print(average)
average = data["temp"].mean()
print(average)
max_num = data["temp"].max()
print(max_num)

# Get Data  in Columns:
print(data["condition"])
print(data.day)

# Get Data in Row:
print(data[data.day == "Monday"])
print(data[data.temp == data["temp"].max()])

monday = data[data.day == "Monday"]
print(monday.condition)
print(monday.temp)
F = (monday.temp * 1.8) + 32
print(F)

# Create a Data frame from scratch:
students = {
    "Alice": {"age": 20, "grade": "A"},
    "Bob": {"age": 22, "grade": "B"},
    "Charlie": {"age": 21, "grade": "A-"},
    "David": {"age": 23, "grade": "B+"},
    "Eva": {"age": 20, "grade": "A+"}
}
data = pandas.DataFrame(students)
print(data)
data.to_csv("new_data.csv")
