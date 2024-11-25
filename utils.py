import re
from nltk.tokenize import sent_tokenize, word_tokenize
import string

def count_syllables(word):
    """
    Count the syllables in a word by identifying vowel clusters

    Parameters:
    word (str): The word for which syllables are to be counted.
    
    Returns:
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
    
    Returns:
    None: Prints the analysis results.
    """

    # Tokenize the text into sentences
    sentences = sent_tokenize(tekst, language='dutch')
    
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
    print(f"Number of sentences: {len(sentences)}")
    print(f"Number of words: {total_words}")
    print(f"Total syllables: {total_syllables}")