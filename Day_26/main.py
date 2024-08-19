import pandas as pd

nato_df = pd.read_csv(r"Day_26\nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}


def make_code(word: str, nato_dict: dict) -> list:
    code_list = [nato_dict[letter] for letter in word]
    return code_list


while True:
    try:
        word = input("Enter a word: ").upper()
        print(make_code(word, nato_dict))
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        break
