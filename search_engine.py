"""
This file contains a Search Engine class which contains methods that work with
the Document
"""
import os
import math
from document import Document
from document import normalize_token


class SearchEngine:
    def __init__(self, saved_queries):
        """
        This function takes a directory and inializes the Search Engine, and gives it
        an inverted index dictionary, a file count in the cirectory, and saves the
        path
        """

        self._i_i = {}
        self._count = 0
        for line in range(len(saved_queries)):
            self._count += 1
            words = saved_queries.loc[line, 'question_column'].split()
            for word in words:
                word = normalize_token(word)
                if word in self._i_i:
                    self._i_i[word].append(line)
                else:
                    self._i_i[word] = [line]
        
    def _calculate_idf(self, word):
        """
        This function takes a word and returns it's inverse
        document frequency. If the word is not in the directory, 
        0 is returned.
        """
        if word in self._i_i.keys():
            return math.log(self._count / len(self._i_i[word]))
        else:
            return 0.0

    def search(self, question):
        """
        This function takes a string query and returns an ordered list
        of the searh engine's documents in the directory, based on how
        relevant they are to the query.
        """
        question = question.split()
        doc_ranking = {}
        for word in question:
            word = normalize_token(word)
            if word in self._i_i.keys():
                docs_with_word = self._i_i[word]
                for doc in docs_with_word:
                    if doc not in doc_ranking.keys():
                        new_frequency = Document(doc).term_frequency(word)
                        doc_ranking[doc] = new_frequency * self._calculate_idf(word)
                    else:
                        doc_ranking[doc] += Document(
                            doc).term_frequency(
                                word) * self._calculate_idf(word)
        values = sorted(doc_ranking.values(), reverse=True)
        doc_final = []
        for value in values:
            for pair in doc_ranking.items():
                doc, num = pair
                if (num == value) and (doc) not in doc_final:
                    doc_final.append(doc)
                    pass
        return doc_final
