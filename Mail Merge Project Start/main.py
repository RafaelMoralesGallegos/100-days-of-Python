PLACEHOLDER = "[name]"

with open(r"Input\Names\invited_names.txt", "r") as file:
    Names = file.readlines()
clean_names = []
for name in Names:
    clean_names.append(name.strip("\n"))

with open(r"Input/Letters/starting_letter.txt") as file:
    template = file.read()

for name in clean_names:
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as file:
        file.write(template.replace(PLACEHOLDER, f"{name}"))
