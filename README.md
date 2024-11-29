# Dutch Text Analysis for Readability Formula

## Overview

This repository analyzes Dutch text to count the number of sentences, words, and syllables. It tokenizes the input text into sentences and words, filters out punctuation marks, and computes syllables in each word to provide statistical analysis. 

The sociologist Flesh(1949) introduced a readability formula for English texts that was later adapted for the Dutch language. The Dutch formula, Flesh-Douma takes the amount of words, syllables and sentences of a text to generate a number between 0 and 100 that refers to the degree of education a reader needs to understand the text. The lower the output of the formula, the more education a reader would need to understand the text. The education degree is also mentioned for the Dutch education system.   

NB do not use this formula for something important since not many factors or variables are taken into account. It is a really basic formula.

## Running the Script:
1. Navigate to the directory containing `utils.py` in your terminal or command prompt.
2. Run the script:
`python utils.py`
3. The script will process each .txt file in the `/data` directory and output the analysis to the terminal.

## Authors
Ariana Britez \
Sjef van Lier