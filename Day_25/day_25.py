# import csv

# with open("Day_25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []

#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

# print(temperatures)

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data['temp'].to_list()
# print(temp_list)

# print(f"The averaage temperature is: {data['temp'].mean()}")
# print(f"The highest temperature recorded wasa: {data['temp'].max()}")

# Get Data from Columns
# print(data[data["day"] == 'Monday'])


# print(data[data["temp"] == data['temp'].max()])

# import pandas as pd

# data = pd.read_csv("weather_data.csv")
# print(data['temp'])
# df_dict = data.to_dict()
# temp_list = data["temp"].to_list()
# average_temp = data["temp"].mean()
# max_temp = data["temp"].max()
# print(f"the Mean Temp is {average_temp}")
# print(f"the Max Temp is {max_temp}")

# # Data from columns
# print(data["condition"])
# print(data.condition)

# # Data from Row
# print(data[data["day"] == "Monday"])
# print(data[data["temp"] == max_temp])

# monday = data[data["day"] == "Monday"]
# temp_monday = (monday.temp[0] * 9 / 5) + 32
# print(f"Monday temperature is {temp_monday} in F")

# data_dict = {"students": ["Amy", "James", "Angela"], "scores": [76, 56, 45]}
# data = pd.DataFrame(data_dict)
# data.to_csv("new_data.csv")
# import pandas as pd

# df = pd.read_csv("squirrel_data.csv")
# fur_color = df["Primary Fur Color"].value_counts()
# df_fc = fur_color.to_frame().reset_index()
# df_fc = df_fc.rename(columns={"Primary Fur Color": "Fur Color"})
# df_fc.to_csv("fur_color.csv")
import sys

print(sys.path)
