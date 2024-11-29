import os
import re
from nltk.tokenize import sent_tokenize, word_tokenize
import string

def count_syllables(word):
    """
    Count the syllables in a word by identifying vowel clusters

    Parameters:
    word (str): The word for which syllables are to be counted.
    
    Return:
    int: The number of syllables in the word.
    """
    
    vowels = "aeiouáéíóúàèìòùäëïöüâêîôû"

    # Count vowel groups as initial syllables
    syllable_count = len(re.findall(rf'[{vowels}]+', word.lower()))
    
    return syllable_count

def analyze_text(tekst):
    """
    Analyze the provided Dutch text to count sentences, words, and syllables.
    
    Tokenize the input text into sentences and words, then count the syllables  in each word. 
    Return the total number of sentences, words, and syllables.
    
    Parameters:
    tekst (str): The text to analyze.
    """

    # Tokenize the text into sentences
    sentences = sent_tokenize(tekst, language='dutch')
    total_sentences = len(sentences)
    
    # Tokenize each sentence into words
    words = [
        [word for word in word_tokenize(sentence, language='dutch') if word not in string.punctuation]
        for sentence in sentences
    ]
    
    # Total number of words in the text
    total_words = sum(len(word) for word in words)
    
    # Count syllables for each word in each sentence
    syllable_counts = [
        [count_syllables(word) for word in sentence] for sentence in words
    ]
    
    # Total syllables in the text
    total_syllables = sum(sum(sentence) for sentence in syllable_counts)
    
    # Output the results
    print(f"Number of sentences: {total_sentences}")
    print(f"Number of words: {total_words}")
    print(f"Total syllables: {total_syllables}")

    return total_sentences, total_words, total_syllables

def readability_formula(total_sentences,total_words, total_syllabels):
    """
    Calculate the Flesch-Douma readability score and determine the target education level based on the result.

    Parameters:
    total_sentences (int): The total number of sentences in the text.
    total_words (int): The total number of words in the text.
    total_syllabels (int): The total number of syllables in the text.

    Return:
    None.
    Print the calculated readability score and the corresponding target education level.
    """

    formula = 206.835-(0.93*(total_words/total_sentences))-(77*(total_syllabels/total_words))
    #keep only two decimals in final outcome
    formula = round(formula, 2)


    if formula <= 30:
        education_level = "academic/professional"
    elif formula > 30 and formula <= 50:
        education_level = "university student"
    elif formula > 50 and formula <= 60:
        education_level = "college advanced secondary education"
    elif formula > 60 and formula <= 70:
        education_level = "secondary school (first years)"
    elif formula > 70 and formula <= 80:
        education_level = "6th grade primary school (groep 8)"
    elif formula > 80 and formula <= 90:
        education_level = "5th grade primary school (groep 7)"
    elif formula > 90 and formula <= 100:
        education_level = "4th grade primary school (groep 6)"
    

    print(f"Flesh-Douma readability formula: {formula}")

    print(f"Target public: {education_level}")
 


def main():
    """
    Main function to analyze all `.txt` files in the `/data` directory.
    
    Iterate through all text files in the `/data` directory, read their content, and perform the text analysis for each file.
    """

    # Define the directory containing the text files
    data_dir = "./data"
    
    # Get a list of all `.txt` files in the directory
    text_files = [file for file in os.listdir(data_dir) if file.endswith(".txt")]
    
    # Process each text file
    for file in text_files:
        file_path = os.path.join(data_dir, file)
        
        # Read the content of the file
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Analyze the text
        print(file)
        sentences, total_words, total_syllables = analyze_text(content)
        print()
        readability_formula(sentences, total_words, total_syllables)
        print('----------------------------------------------')
        print()

if __name__ == "__main__":
    main()