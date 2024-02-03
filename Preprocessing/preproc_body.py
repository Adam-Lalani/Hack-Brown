
import spacy
import nltk
import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer 
import unicodedata
import string
import pandas as pd 


def proc_paragaph(s): 

    output = ""

    # remove punctuation 
    string_no_punct=re.sub(r'[^\w\s]','',s)
    output = string_no_punct
    
    # remove stop words 
    stopwords_list = stopwords.words('english')
    string_no_stopwords = [word for word in  output.split() if (word not in stopwords_list) and len(word) < 30]
    string_no_stopwords = " ".join(string_no_stopwords)

    output = string_no_stopwords
    
    output = re.sub(' +', ' ', output).strip()

    lemmatizer = WordNetLemmatizer()

    output  = lemmatizer.lemmatize(output)

    return output

# df = pd.read_csv('emails.csv')
# df['Data'] = df['Data'].apply(proc_paragaph)
# print(df.head(1)['Data'])

# df.to_csv('emails_proc.csv', index=False)