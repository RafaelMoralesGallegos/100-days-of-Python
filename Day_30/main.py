# try:
#     file = open("Day_30/a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("Day_30/a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"That key {error_message} does not Exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     raise TypeError("This is an error I made up.")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height sholuld not be over 3 meters.")

bmi = weight / height**2
print(bmi)
