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

# Output:
It creates:

> a dataframe with the details of frequency ranges and number of tokens in that range

> a pie chart with the percentage of the text for each frequency range

> a bar chart that compares number of words in the text, lexical variability and lexical density

> a word cloud pointing at the most used words

# Some recommendations:
Make sure the text file is correctly encoded in utf-8.

# Visualization examples:
![pie_chart_profile](https://user-images.githubusercontent.com/20560202/110121570-8d08f500-7d8c-11eb-86b4-12efdaa88e5b.png)
