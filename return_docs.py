# import files
import sys
import os
import pandas as pd

# Get the path of the parent directory of the current file
parent_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory to the system path
sys.path.insert(0, parent_dir)

# import ranker module
from nlp import ranker

# Pass query to the ranker
def get_docs_for_query(query: str) -> dict:

    # Get the relevant documents
    ranking_df = ranker.return_relevant_to_query(query)

    # Assuming ranking_df has a column 'Relevance Score' and an index corresponding to document indices
    # Sort the DataFrame by 'Relevance Score' in descending order
    sorted_ranking_df = ranking_df.sort_values(by='Cosine Similarity', ascending=False)

    # Retrieve the indices of the top n documents
    n = 3
    top_n_indices = sorted_ranking_df.head(n).index.tolist()

    # # Output the indices
    # print("Indices of Top 3 Documents:", top_n_indices)

    # Now get the entries with these indices from emails_proc.csv and save them as dicts with fields for Subject and Data

    # Read the CSV into a DataFrame
    df = pd.read_csv('/Users/morganlo/hackBrown/Hack-Brown/nlp/input_data/emails_proc.csv')

    # filter to the indices in top_n_indices
    top_n_df = df.iloc[top_n_indices]

    # Convert the DataFrame to a list of dictionaries
    top_n_docs = top_n_df.to_dict(orient='records')

    return top_n_docs


# Example usage
query = "I want to go to a cool event where I can learn how to get a job in software engineering and big tech that will help me make a lot of money"
response = get_docs_for_query(query)
print(response)

