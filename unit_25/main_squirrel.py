# separate the squirrels in colours.
import pandas

data = pandas.read_csv("Squirrel_Data.csv")
gray_squirrel = data[data["Primary Fur Color"] == "Gray"]
print(gray_squirrel)

gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
print(gray_squirrel_count)