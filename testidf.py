#testing tf-idf on small scale data. will eventually be deleted from the repository

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
 
# this is a very toy example, do not try this at home unless you want to understand the usage differences
docs=["the house had a tiny little mouse",
      "the cat saw the mouse",
      "the mouse ran away from the house",
      "the cat finally ate the mouse",
      "the end of the mouse story"
     ] 
#instantiate CountVectorizer()
cv=TfidfVectorizer(use_idf=True,min_df=2,max_df=10)
 
# this steps generates word counts for the words in your docs
word_count_vector=cv.fit_transform(docs)


vectorizer = TfidfVectorizer(use_idf=True)
vectorizer1 = TfidfVectorizer(use_idf=True,min_df=2,max_df=10)
tfidf_result = vectorizer.fit_transform(docs)

# get the first vector out (for the first document)
first_vector_tfidfvectorizer=tfidf_result[0]
 
# place tf-idf values in a pandas data frame
df = pd.DataFrame(first_vector_tfidfvectorizer.T.todense(), index=vectorizer.get_feature_names(), columns=["tfidf"])
end_result = df.sort_values(by=["tfidf"],ascending=False)
print(end_result)
x = 4