import pandas

data = pandas.read_csv("Squirrel_Data.csv")
gray_squirrels_count = len(data[data["fur_color"] == "Gray"])
red_squirrels_count = len(data[data["fur_color"] == "Cinnamon"])
black_squirrels_count = len(data[data["fur_color"] == "Black"])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count,red_squirrels_count,black_squirrels_count]
}
print(data_dict)
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")