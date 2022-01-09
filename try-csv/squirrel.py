import pandas as pd

data = pd.read_csv('./squirrel_data.csv')
grey_sqs = data[data['Primary Fur Color'] == "Gray"]
count_grey = len(grey_sqs)

black_sqs = data[data['Primary Fur Color'] == "Black"]
count_black = len(black_sqs)

cinnamon_sqs = data[data['Primary Fur Color'] == "Cinnamon"]
count_cinnamon = len(cinnamon_sqs)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [len(grey_sqs), len(cinnamon_sqs), len(black_sqs)]
}

df = pd.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")