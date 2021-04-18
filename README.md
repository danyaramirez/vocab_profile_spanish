# Vocabulary Profile for Spanish Texts

# Overview
This tools provides a visualization of the vocabulary profile of texts in Spanish.

# What is "vocabulary profile"?
Vocabulary profile is defined here as the characteristics of a text (text file) regarding the use frequency of the words in the text (c.f. Mark Davies' Corpus del Español). Also, we include the ratio of unique word per total number of words (lexical variability), and the ratio of unique content words per total number of content words (lexical density).  This is a useful tool for Spanish language teachers to know the general level of difficulty their texts convey.

# Basic characteristics:
The code was created in Python 3.8.

The repo includes:
> A .py file with the code

> A .csv file with the corpus list

> A .csv file with semantic categorization of corpus tokens

> An example text with fragments of "Cien años de soledad" by Gabriel García Márquez

# Output:
It creates:

> a dataframe with the details of frequency ranges and number of tokens in that range

> a tree map with the proportions of the text for each frequency range

> a bar chart that compares number of words in the text, lexical variability and lexical density (and a dataframe with details)

> a word cloud pointing at the most used content words

# Some recommendations:
Make sure the text file is correctly encoded in utf-8.

# Visualization examples:
![barchart](https://user-images.githubusercontent.com/20560202/115150264-9ea11600-a035-11eb-8668-81bf6c22e61b.png)
![treemap](https://user-images.githubusercontent.com/20560202/115150276-a791e780-a035-11eb-9d9a-f9265febd8b1.png)
![wordcloud](https://user-images.githubusercontent.com/20560202/115150277-ac569b80-a035-11eb-82f7-0f7257149ff3.png)



