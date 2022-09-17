#필요한 라이브러리 import
try:
    import numpy
    import pandas as pd
    import pickle as pk
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    import re
    from nltk.stem.snowball import SnowballStemmer
    import nltk
    nltk.download('all')
    stemmer = SnowballStemmer("english")
except ImportError:
    print('You are missing some packages! ' \
          'We will try installing them before continuing!')
    !pip install "numpy" "pandas" "sklearn" "nltk"
    import numpy
    import pandas as pd
    import pickle as pk
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    import re
    from nltk.stem.snowball import SnowballStemmer
    import nltk
    stemmer = SnowballStemmer("english")
    print('Done!')


#articles 나누고, nan제거

def user(news_articles):
    news_articles = news_articles[['title','text']].dropna()
    articles = news_articles['text'].tolist()
    return articles

#불용어 및 태깅 제거
def clean_text(document):
    document = re.sub('[^\w_\s-]', ' ',document)       #remove punctuation marks and other symbols
    document = re.sub('<.+?>', '', document, 0, re.I|re.S)
    #document = re.sub('&nbsp;| |\t|\r|', '', document)
    tokens = nltk.word_tokenize(document)              #Tokenize 
    cleaned_article = ' '.join([stemmer.stem(item) for item in tokens])    #Stemming
    cleaned_articles = list(map(clean_text, articles))
    return cleaned_articles


def user_read(ARTICLES_READ):
    user_articles = ' '.join(cleaned_articles[i] for i in ARTICLES_READ)
    return user_articles

#TF-IDF(읽은 것, 안 읽은 것)

def TF-IDF_matrix(cleaned_articles):
    tfidf_matrix = TfidfVectorizer(stop_words='english', min_df=2) 
    article_tfidf_matrix = tfidf_matrix.fit_transform(cleaned_articles)
    return article_tfidf_matrix

def cosine_sim(user_articles):
    
    user_article_tfidf_vector = tfidf_matrix.transform([user_articles])
    articles_similarity_score=cosine_similarity(article_tfidf_matrix, user_article_tfidf_vector)
    recommended_articles_id = articles_similarity_score.flatten().argsort()[::-1]
    final_recommended_articles_id = [article_id for article_id in recommended_articles_id 
                                 if article_id not in ARTICLES_READ ][:NUM_RECOMMENDED_ARTICLES]
    return final_recommended_articles#추천

def recommed_art(news_articles, ARTICLES_READ,final_recommended_articles_id):
    #Recommended Articles and their title
    print ('Articles Read')
    print (news_articles.loc[ARTICLES_READ]['title'])
    print ('\n')
    print ('Recommendations ')
    print (news_articles.loc[final_recommended_articles_id]['title'])
