import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dic = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_code():
    word = input("Enter a word: ").upper()
    try:
        word_list = [phonetic_dic[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet are allowed.")
        generate_code()
    else:
        print(word_list)


generate_code()
