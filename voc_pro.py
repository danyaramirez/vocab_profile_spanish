# Python 3.8
# Make sure encoding of text is utf-8

import pandas as pd
import re
import numpy as np
import matplotlib.pyplot as plt
import squarify


# Create a data frame out of the Corpus del Español.
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

#Merge word data frame with corpus data frame to have corpus frequency of each word
df = words.merge(corpus, how="left", on=[0])
df.dropna(axis = 0, inplace=True)
df = df.rename(columns={0: "token", 1: "freq_order" })

# Create data frame for bucketing count
freq = np.array([["1 to 300", 0], ["301 to 1000", 0], ["1001 to 2000" , 0], ["2001 to 3000" , 0],
              ["3001 to 5000", 0], ["5001 to 10000", 0], ["10001 to 25000", 0],
              ["25001 to 50000", 0], ["50001 to 100000", 0], ["100000 and higher", 0]])
token_freq = pd.DataFrame(freq, columns = ['Frequency in corpus', 'Number of tokens per frequency'])

# Define number of tokens with particular frequency.
tk = token_freq['Number of tokens per frequency']
tk[0] = df.query("freq_order > 0 and freq_order <= 300").count()[0]
tk[1] = df.query("freq_order > 300 and freq_order <= 1000").count()[0]
tk[2] = df.query("freq_order > 1000 and freq_order <= 2000").count()[0]
tk[3] = df.query("freq_order > 2000 and freq_order <= 3000").count()[0]
tk[4] = df.query("freq_order > 3000 and freq_order <= 5000").count()[0]
tk[5] = df.query("freq_order > 5000 and freq_order <= 10000").count()[0]
tk[6] = df.query("freq_order > 10000 and freq_order <= 25000").count()[0]
tk[7] = df.query("freq_order > 25000 and freq_order <= 50000").count()[0]
tk[8] = df.query("freq_order > 50000 and freq_order <= 100000").count()[0]
tk[9] = df.query("freq_order > 100000").count()[0]

# Writing a csv file with all the vocabulary profile for these 9 buckets.
token_freq.to_csv('freq_profile.csv', index=False, index_label=None)

# Visualizations:
# (i) pie chart with number of tokens in each frequency range

# Simplify data frame to have only 7 slices in the pie chart
simple_array = np.array([["1 to 300", 0], ["301 to 1000", 0], ["1001 to 3000" , 0],
              ["3001 to 5000", 0], ["5001 to 10000", 0], ["10001 to 50000", 0], ["50001 and higher", 0]])
token_freq_small = pd.DataFrame(simple_array, columns = ['Frequency in corpus', 'Tokens per frequency'])

token_freq_small["Tokens per frequency"][0] = token_freq["Number of tokens per frequency"][0]
token_freq_small["Tokens per frequency"][1] = token_freq["Number of tokens per frequency"][1]
token_freq_small["Tokens per frequency"][2] = token_freq["Number of tokens per frequency"][2] +\
                                              token_freq["Number of tokens per frequency"][3]
token_freq_small["Tokens per frequency"][3] = token_freq["Number of tokens per frequency"][4]
token_freq_small["Tokens per frequency"][4] = token_freq["Number of tokens per frequency"][5]
token_freq_small["Tokens per frequency"][5] = token_freq["Number of tokens per frequency"][6] +\
                                              token_freq["Number of tokens per frequency"][7]
token_freq_small["Tokens per frequency"][6] = token_freq["Number of tokens per frequency"][8] +\
                                              token_freq["Number of tokens per frequency"][9]

# Build treemap using token_fre_small
volume = token_freq_small["Tokens per frequency"]
labels = ["1 to 300", "301 to\n 1000", "1,001 to\n 3,000", "3,001 to\n 5,000",
          "5,001 to\n 10,000", "10,001 to\n 50,000", "50,001 and\n higher"]
color_list = ['#65C1E8', '#D85B63', '#D680AD','#5C5C5C','#C0BA80','#FDC47D','#EA3B46']

plt.rc('font', size=12)
squarify.plot(sizes=volume, label=labels,
              color=color_list, alpha=0.7)
plt.axis('off')
plt.title("Tokens in Text per Frequency Range in Spanish ")

plt.show()

# (ii) number of tokens, lexical variability, lexical density

# Import file to calculate lexical density
category = pd.read_csv("corpus_category.csv", sep=";")
# Combine category and df
result = pd.merge(df, category, on="token")
# Calculate lexical density (number of unique content words)
density = result.query("cat1 == 'v' or cat1 == 'n' or cat1 == 'j' or cat1 =='r'")
# Create dataframe for all n of tokens, lex dens, lex var
info = {'Feature': ["Number of tokens", "Count for lexical variability", "Count for lexical density"], 
          'Proportion': [df["token"].count(), df["token"].nunique(), density["token"].nunique()]}
bar_df = pd.DataFrame(data=info)

# Create simple horixontal barplot for n tokens, lex dens, and lex var
plt.barh(data=bar_df, y="Feature", width="Proportion")
plt.title("Count of tokens - total, tokens for Lexical Variability, and tokens for Lexical Density in text")
plt.show();


# (iii) word cloud

