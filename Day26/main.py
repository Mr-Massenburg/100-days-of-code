# Day 26 | Nato Phonetic Alphabet - List and dictionary comprehension 
# Converts a word into its NATO phonetic code using pandas

import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

alpha_dict = {row.letter:row.code for row in df.itertuples()}

word = input("Enter a word: ").upper()
alpha_list = [alpha_dict[char] for char in word]
print(alpha_list)
