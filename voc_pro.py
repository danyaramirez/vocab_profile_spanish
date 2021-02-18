# Python 3.8
# Make sure encoding of text is utf-8

# Import necessary packages
import pandas as pd
import re

# Create a data frame out of Mark Davies' Corpus del Español.
corpus = pd.read_csv("Corpus_voc_pro.csv", header=None)

# Import text to analize and assign text into a variable
text = open("example2.txt", "r", encoding="utf8")
content = text.read()
#Create list of tokens - words and symbols - extracted from text with all characters:
char_list = content.split()

#Create function to remove all characters that are not part of the Spanish alphabet (keep accent marks)
def symbol_free(list):
    word_list = []
    for i in list:
        new_word = re.sub("[^a-zA-ZñÑáéíóúÁÉÍÓÚ]+", "", i)
        if new_word != "":
            word_list.append(new_word)
    return word_list

#Apply function to the list of tokens with all characters
word_list = symbol_free(char_list)

#Convert list into Pandas data frame
words = pd.DataFrame(word_list)

#Merge word data frame with corpus data frame to have frequency of each word
df = words.merge(corpus, how="left", on=[0])
df.dropna(axis = 0, inplace=True)