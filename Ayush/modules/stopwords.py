class stopwords:
    def __init__(self,tokens):
        self.tokens = tokens
    
    def stopword_removal(self):
        f = open(r'C:\Users\ayush\Nepali language processing\modules\nlp_data\stopwords.txt','r',encoding='utf-8')
        stopwords_list = f.read()
        new_tokens = list() #new_tokens hold the list of words after removing stopwords
        for token in self.tokens:
            if token not in stopwords_list:
                new_tokens.append(token)

        return new_tokens

    def __str__(self):
        return "returns the tokens after removing stopwords"
