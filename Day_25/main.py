import numpy as np
import pandas as pd

# data = pd.read_csv(r"Day_25\weather_data.csv")

# new_dict = data.to_dict()
# # print(new_dict)

# temp_list = data["temp"].to_list()
# # print(data["temp"].mean())
# # print(np.mean(temp_list))

# # print(data["temp"].max())
# # print(np.max(temp_list))

# # print(data["condition"])
# # print(data.condition)

# # print(data[data.temp == data.temp.max()])
# monday_temp = (9 / 5) * int(data[data.day == "Monday"].temp.iloc[0]) + 32
# print(monday_temp)

df = pd.read_csv(r"Day_25\squirrel_data.csv")
fur_color = df["Primary Fur Color"].value_counts()
df_fur = fur_color.reset_index()
df_fur.columns = ["Primary Fur Color", "Count"]
df_fur.to_csv(r"Day_25\Fur_color.csv")
