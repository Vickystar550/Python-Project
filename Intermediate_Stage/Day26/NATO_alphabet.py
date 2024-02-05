import pandas

alphabet_df = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet_mapped = {row.letter: row.code for (index, row) in alphabet_df.iterrows()}

user = input("Enter your name:\t").upper()

result = [alphabet_mapped[i] for i in user]

print(result)
