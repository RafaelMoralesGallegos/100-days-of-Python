import random

name = "angela"
letters_list = [letter for letter in name]
# print(letters_list)


double_numbers = [n * 2 for n in range(1, 5)]
# print(double_numbers)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {student: random.randint(1, 100) for student in names}

passing_students = {
    student: score for (student, score) in student_scores.items() if score >= 60
}
# print(passing_students)

# *Part 1
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# 🚨 Don't change code above 👆
# Write your code below 👇

words = sentence.split()

result = {word: len(word) for word in words}
# print(result)

# *Part 2
weather_c = eval(
    '{"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}'
)
# 🚨 Don't change code above 👆
# Write your code 👇 below:


def celcius_fahrenheit(degree: int) -> float:
    fahrenheit = (9 / 5) * degree + 32
    return fahrenheit


weather_f = {day: celcius_fahrenheit(weather) for (day, weather) in weather_c.items()}

# print(weather_f)
