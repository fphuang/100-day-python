import pandas

# data = pandas.read_csv("./weather_data.csv")
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
# print(int(monday.temp) * 9 / 5 + 32)
#

data_dict = {
    "students": ["Amy", "Alice", "Angela"],
    "scores": [76, 56, 65]
}

df = pandas.DataFrame(data_dict)
df.to_csv("new_data.csv")
