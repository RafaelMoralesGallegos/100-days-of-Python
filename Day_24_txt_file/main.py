# with open("D:/Documentos/Python/100_days_of_Python/Day_24/my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# * if file not exist and mode is Wright then new file is created
with open("new_file.txt", mode="w") as file:
    file.write("\nNew text.")
