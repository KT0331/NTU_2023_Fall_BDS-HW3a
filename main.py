﻿
import camelot
import re
import numpy as np

class pdf2text:
    def __init__(self):
        pass

    def __call__(self, pdf_file):
        tables = camelot.read_pdf(pdf_file, pages="all")
        texts = []
        i = 0
        
        for table in tables:
            text = []
            text.append(table.df.to_string())
            str_text = " ".join(text)
            str_text = str_text.replace("\\n", "")
            text = str_text.split()
            texts.insert(i, " ".join(text))
            i += 1
        return texts


class text2vector:
    def __init__(self):
        pass

    def __call__(self, text):
        # Tokenize the text into words
        words = re.findall(r'\b\w+\b', text.lower())
        # Create a dictionary with unique words and their frequencies
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
        return word_freq


class cosine_sim:
    def __init__(self):
        pass

    @staticmethod
    def similar_words(word1, word2):
        # Check if one word is a subset of the other
        return set(word1).issubset(set(word2)) or set(word2).issubset(set(word1))

    def __call__(self, vector_from_table, vector_from_keyword):
        # Calculate cosine similarity considering similar words
        dot_product = sum(
            (
                vector_from_table.get(word, 0) * vector_from_keyword.get(sim_word, 0)
                for word in set(vector_from_table)
                for sim_word in vector_from_keyword
                if self.similar_words(word, sim_word)
            )
        )
        norm_table = np.linalg.norm(list(vector_from_table.values()))
        norm_keyword = np.linalg.norm(list(vector_from_keyword.values()))
        similarity = dot_product / (norm_table * norm_keyword) if norm_table * norm_keyword != 0 else 0
        return similarity


def main(keyword, pdf_file):
    pdf_parser = pdf2text()
    table_text = pdf_parser(pdf_file)

    keyword_vectorizer = text2vector()
    keyword_vector = keyword_vectorizer(keyword)
    
    # Split the text into tables and calculate similarity
    similarity_calculator = cosine_sim()

    max_similarity = 0
    most_similar_table = ""

    for table in table_text:
        table_vector = text2vector()(table)
        keyword_found = False
        keyword_vector_found = False

        for word in table_vector:
            if word == keyword:
                keyword_found = True
                if not keyword_vector_found:
                    keyword_vector_found = True
                    similarity = similarity_calculator(table_vector, keyword_vector)

                    if similarity > max_similarity:
                        max_similarity = similarity
                        most_similar_table = table
                        break

    if max_similarity > 0:
        print("Most similar text table:")
        print(most_similar_table)
        print("Similarity:", max_similarity)
    else:
        print("Keyword not found in the table.")
        print("Similarity:", max_similarity)

if __name__ == "__main__":
    keyword = '非監督式'
    #keyword = '發現數據中隱藏的結構'
    # Call the main function with sample keyword and PDF file paths
    main(keyword, "ai_tables_#1.pdf")
    main(keyword, "ai_tables_#2.pdf")
