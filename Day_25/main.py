import pandas as pd

data = pd.read_csv("/home/vinycius/Programacao/Python/100-Days-of-Code/Day_25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])

data_dict = {
    "Fur Color": ["Gray", "Black", "Cinnamon"],
    "Count": [gray_squirrels_count, black_squirrels_count, cinnamon_squirrels_count]
}

squirrels_count = pd.DataFrame(data_dict)

squirrels_count.to_csv("/home/vinycius/Programacao/Python/100-Days-of-Code/Day_25/squirrels.csv")

print(squirrels_count)
