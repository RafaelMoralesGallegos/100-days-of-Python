file1 = []
file2 = []

with open(r"file1.txt", "r") as file:
    for line in file:
        file1.append(int(line))

with open(r"file2.txt", "r") as file:
    for line in file:
        file2.append(int(line))

result = [n for n in file1 if n in file2]

print(result)
