class Tf_idf:

    def __init__(self):
        4+5

    def tfidf_features(data, papers, ngrams=2, features=None):

        df_temp = data.copy(deep=True)
        df_temp = basic_preprocessing(df_temp)

        papers_temp = papers.copy(deep=True)
        papers_temp = basic_preprocessing(papers_temp)

        tfidf_vectorizer = TfidfVectorizer(ngram_range=(1, ngrams), max_features=features)

        corpus = df_temp['lemma'].append(papers_temp['lemma'])
        tfidf_vectorizer.fit(corpus)

        data_corpus = df_temp["lemma"].tolist()
        paper_corpus = papers_temp["lemma"].tolist()

        data = tfidf_vectorizer.transform(data_corpus)
        papers = tfidf_vectorizer.transform(paper_corpus)

        return data, papers


    def tfidf(data, papers, ngrams=2, labels=True):

        df_temp = data.copy(deep=True)
        df_temp = basic_preprocessing(df_temp)

        papers_temp = papers.copy(deep=True)
        papers_temp = basic_preprocessing(papers_temp)

        tfidf_vectorizer = TfidfVectorizer(ngram_range=(1, ngrams))

        corpus = df_temp['lemma'].append(papers_temp['lemma'])
        tfidf_vectorizer.fit(corpus)

        list_corpus = corpus.tolist()

        data_corpus = df_temp["lemma"].tolist()
        paper_corpus = papers_temp["lemma"].tolist()

        data = tfidf_vectorizer.transform(data_corpus)
        papers = tfidf_vectorizer.transform(paper_corpus)

        return data, papers
