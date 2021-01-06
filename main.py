import pandas as pd


data = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_alphabet = {row.letter:row.code for (index, row) in data.iterrows()}


word = input("Enter a word: ").upper()


code_words = [phonetic_alphabet[letter] for letter in word if letter in phonetic_alphabet]
print(code_words)
