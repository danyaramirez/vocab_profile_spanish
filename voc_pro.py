# python 3.5
# TODO make dynamic, figure out name of files so they dont replace themselves

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import csv  # to be able to work with .csv
import os  # to be able to find the files in the current folder

# Creating a dictionary out of the Corpus del Español.
reader = csv.reader(open("Corpus_voc_pro.csv", "r"))
dictionary = {}
for row in reader:
    token, frequency = row
    if token in dictionary.keys():
        pass
    else:
        dictionary[token] = frequency


# Function to create the vocabulary profile
def vocprofile(lista):
    # Creating a list that includes the values for all keys in the dictionary
    # that are in the list "lista."
    frequencies = []
    for word in lista:
        word = word.lower()
        if word in dictionary.keys():
            frequencies.append(dictionary[word])
        else:
            pass

    # Creating lists for displaying the information in a pi chart.
    labels = ["1 to 300", "301 to 1000", "1001 to 2000", "2001 to 3000",
              "3001 to 5000", "5001 to 10000", "10001 to 25000",
              "25001 to 50000", "50001 to 100000"]
    values = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Adding each value (sum of keys in each bucket) to their key in the
    # dictionary.
    for number in frequencies:
        if 1 <= int(number) <= 300:
            values[0] = values[0] + 1
        elif 301 <= int(number) <= 1000:
            values[1] = values[1] + 1
        elif 1001 <= int(number) <= 2000:
            values[2] = values[2] + 1
        elif 2001 <= int(number) <= 3000:
            values[3] = values[3] + 1
        elif 3001 <= int(number) <= 5000:
            values[4] = values[4] + 1
        elif 5001 <= int(number) <= 10000:
            values[5] = values[5] + 1
        elif 10001 <= int(number) <= 25000:
            values[6] = values[6] + 1
        elif 25001 <= int(number) <= 50000:
            values[7] = values[7] + 1
        elif 50001 <= int(number) <= 100000:
            values[8] = values[8] + 1
        else:
            pass
    # Writing a csv file with all the vocabulary profile for these 9 buckets.
    with open("output.csv", "a") as fp:
        wr = csv.writer(fp, dialect='excel')
        wr.writerow([file_name]+values)


# Opening every file in the folder and store the content in a variable.
folder = os.listdir("Textos")
for f in sorted(folder):
    if f == ".DS_Store":
        continue
    file_name = os.path.splitext(os.path.basename(f))[0]
    texto_original = open("Textos/" + f).read()
    lista = word_tokenize(texto_original)
    vocprofile(lista)
