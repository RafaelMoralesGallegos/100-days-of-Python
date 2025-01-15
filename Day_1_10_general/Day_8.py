def calculate_love_score(name1, name2):
    names = f"{name1.lower()}{name2.lower()}"
    true_value = 0
    love_value = 0
    for letter in names:
        if letter in "true":
            true_value += 1

        if letter in "love":
            love_value += 1

    print(int(f"{true_value}{love_value}"))


calculate_love_score("Kanye West", "Kim Kardashian")
