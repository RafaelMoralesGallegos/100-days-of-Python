file1 = []
file2 = []

with open(r"file1.txt", "r") as file:
    for line in file:
        file1.append(int(line))

with open(r"file2.txt", "r") as file:
    for line in file:
        file2.append(int(line))

result = [n for n in file1 if n in file2]

# print(result)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = sentence.split()
result = {word: len(word) for word in result}
# print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}


def temp_f(temp_c):
    temp = (temp_c * 9 / 5) + 32
    return temp


weather_f = {day: temp_f(temp) for day, temp in weather_c.items()}

print(weather_f)
