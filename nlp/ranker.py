import pandas as pd
import nltk
from nltk.corpus import wordnet as wn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer

def return_relevant_to_query(query):

    ### 
    # Now with tf_idf matrix and relative frequencies, we can calculate cosine similarity between query and documents
    ### 

    # File paths for the CSV files
    tfidf_matrix_file_path = 'nlp\\written_data\\tfidf_matrix.csv'  

    # Load the TF-IDF matrix
    tfidf_df = pd.read_csv(tfidf_matrix_file_path)
    # print("Dimensions of TF-IDF DataFrame:", tfidf_df.shape)


    # Extract feature names and the matrix
    feature_names = tfidf_df.columns[1:]  # Skip the index column
    tfidf_matrix = tfidf_df[feature_names].values
    # print("Dimensions of TF-IDF Matrix:", tfidf_matrix.shape)
  
    # Function to generate synonyms using WordNet
    def get_synonyms(word):
        synonyms = set()
        for syn in wn.synsets(word):
            for lemma in syn.lemmas():
                synonyms.add(lemma.name())
        return list(synonyms)

    synonym_list = [get_synonyms(word) for word in query.split()]
    flattened_list = [word for sublist in synonym_list for word in sublist]
    # print("Number of words after flattening synonyms:", len(flattened_list), flattened_list)

    # Vectorize the query
    # Note: We are using TfidfVectorizer here to approximate. Ideally, use the same vectorizer used for creating the TF-IDF matrix.
    vectorizer = TfidfVectorizer(vocabulary=feature_names)

    # Load IDF scores
    # Load IDF scores from CSV
    idf_df = pd.read_csv('nlp\\written_data\\idf_df.csv')
    idf_dict = dict(zip(idf_df['Token'], idf_df['IDF']))

    # Count frequency of each token in flattened_list
    token_freq = Counter(flattened_list)

    # Calculate TF (term frequency) for each token
    total_tokens = len(flattened_list)
    tf_dict = {token: count / total_tokens for token, count in token_freq.items()}

    # Calculate TF-IDF scores
    tfidf_dict = {token: tf_dict.get(token, 0) * idf_dict.get(token, 0) for token in token_freq}

    from scipy.sparse import csr_matrix

    # Create a sparse matrix for the query vector
    # Assuming feature_names is a list of all tokens in the same order as in tfidf_matrix
    query_vector_data = [tfidf_dict.get(feature, 0) for feature in feature_names]
    query_vector = csr_matrix(query_vector_data)




    # Compute cosine similarity between query and documents
    cosine_similarities = cosine_similarity(query_vector, tfidf_matrix).flatten()
    # print("Dimensions of Cosine Similarities:", cosine_similarities.shape)

    # Output the cosine similarity scores
    # print("Cosine Similarity Scores:", cosine_similarities, sum(cosine_similarities))

    # Write the cosine similarity scores to a CSV file
    # Create a DataFrame with cosine similarities and document indices
    cosine_similarity_df = pd.DataFrame({
        'Document Index': tfidf_df.index - 1,
        'Cosine Similarity': cosine_similarities
        })



    # cosine_similarity_df.to_csv('nlp\\written_data\\cosine_similarity.csv', index=False)

    return cosine_similarity_df





