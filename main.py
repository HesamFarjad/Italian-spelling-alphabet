from turtle import Turtle, Screen
import pandas

# image =""
# t = Turtle()
# t.penup()
# t.hideturtle()
# screen = Screen()
# screen.addshape()
# t.shape()

# Comprehension List + Comprehension Dictionary
data = pandas.read_csv("nato_phonetic_alphabet.csv")
new_dic = {row.letter: row.code for (index, row) in data.iterrows()}
# print(new_dic)
name_inserted = input("Insert a word :").upper()
final_alph_name = [new_dic[i] for i in name_inserted]
print(final_alph_name)



# screen.exitonclick()
