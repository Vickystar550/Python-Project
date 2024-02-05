import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240205.csv")


fur_color = data["Primary Fur Color"]
ls

grey_count = fur_color[fur_color == 'Gray'].count()
red_count = fur_color[fur_color == 'Cinnamon'].count()
black_count = fur_color[fur_color == 'Black'].count()

solved_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [grey_count, red_count, black_count]
}

df = pandas.DataFrame(solved_dict)
print(df)

df.to_csv("squirrel_count.csv")
