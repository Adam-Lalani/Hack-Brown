import pandas as pd
import numpy as np
import math
import nltk
from nltk.corpus import wordnet as wn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer

# # Ensure you have the required NLTK data
# nltk.download('wordnet')
# nltk.download('punkt')

# Load documents from a CSV file
csv_file_path = '/Users/morganlo/hackBrown/Hack-Brown/nlp/input_data/emails_proc.csv' 
# Read the CSV into a DataFrame
df = pd.read_csv(csv_file_path)
doc_list = [f"{row['Subject']}{row['Data']}" for index, row in df.iterrows()]

# Preprocess documents (as an example, lowercasing here)
processed_documents = [doc.lower() for doc in doc_list]

# Calculate TF-IDF and then Cosine Similarity
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(processed_documents)

# Store tfidf_matrix as csv in same directory
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())
tfidf_df.to_csv('/Users/morganlo/hackBrown/Hack-Brown/nlp/written_data/tfidf_matrix.csv', index=False)

## Calculate frequency of tokens in doc list

# Tokenize and count occurrences
# print("Processed Documents:", processed_documents)

vectorizer = CountVectorizer(binary=True)
X = vectorizer.fit_transform(processed_documents)
# print('X',X)
tokens = vectorizer.get_feature_names_out()
# print('tokens', tokens)

# Calculate the document frequency for each term
doc_freq = np.sum(X.toarray(), axis=0)

# Calculate IDF for each term
# Adding 1 to the denominator for smoothing and avoiding division by zero
idf_vector = np.log((len(processed_documents) + 1) / (doc_freq + 1)) + 1

# Combine tokens and their IDF values
idf_scores = list(zip(tokens, idf_vector))

# Convert to DataFrame
idf_df = pd.DataFrame(idf_scores, columns=['Token', 'IDF'])

# File path to save the CSV
filepath = 'nlp\written_data\idf_df.csv'

# Write the DataFrame to CSV
idf_df.to_csv(filepath, index=False)

 











