import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dic = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()
word_list = [phonetic_dic[letter] for letter in word]
print(word_list)
