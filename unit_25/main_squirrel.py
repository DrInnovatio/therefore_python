# separate the squirrels in colours.
import pandas

data = pandas.read_csv("Squirrel_Data.csv")
gray_squirrel = data[data["Primary Fur Color"] == "Gray"]
print(gray_squirrel)

gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrel_count)
print(red_squirrel_count)
print(black_squirrel_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
print(df)