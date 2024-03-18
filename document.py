"""
This file has a Document class which has functions including an initializer,
term_frequency, get-path, get_words, which are all to do with taking a file
"""

import re
import MySQLLink


class Document:
    def __init__(self, index):
        """
        This function initializes the Document Object,
        and gives it the fields Term_Frequency and Path
        """
        MySQL = MySQLLink.SQLLink()
        words = MySQL.get_data().loc[index, 'question_column']
        term_frequency = {}
        count = 0
        for word in words.split():
            count += 1
            word = normalize_token(word)
            if word not in term_frequency.keys():
                term_frequency[word] = 0
            term_frequency[word] += 1
        for key in term_frequency:
            term_frequency[key] /= count
        self._tf = term_frequency
        self._path = index

    def term_frequency(self, word):
        """
        This function takes a Document object and a word and returns
        how often that word occurs. If it is not in the document, it returns 0
        """
        normalize_token(word)
        if word in self._tf.keys():
            return self._tf[word]
        return 0

    def get_path(self):
        """
        This function takes a Document object and returns the file path to the file
        """
        return self._path

    def get_words(self):
        """
        This function takes a Document object and returns a list of words
        contained within the doc
        """
        return list(self._tf.keys())


def normalize_token(token):
    """
    This function takes a string and removes any punctuation or capitals
    """
    if '?' in token:
        token = token[: token.find('?')] + token[token.find('?') + 1 :]
    return re.sub(r"\W+", "", token.lower())
