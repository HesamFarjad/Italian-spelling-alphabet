import pandas

# Comprehension List + Comprehension Dictionary
data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dic = {row.letter: row.code for (index, row) in data.iterrows()}

go_on = True

while go_on:
    try:
        name_inserted = input("Insert a word :").upper()
        final_alph_name = [new_dic[i] for i in name_inserted]
    except KeyError:
        print("Please enter a valid value (Character).")
    else:
        print(final_alph_name)
        go_on = False
