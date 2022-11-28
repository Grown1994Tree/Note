import re
import string
import jieba

class Normalization:
    def __init__(self):
        with open("dict/stop_words.utf8", encoding="utf8") as f:
            self.stopword_list = f.readlines()
    
    def tokenize_text(self, text):
        tokens = jieba.lcut(text) # 分词
        tokens = [token.strip() for token in tokens] # 去除空格
        
        return tokens
    
    def remove_special_characters(self, text):
        tokens = self.tokenize_text(text)
        pattern = re.compile('[{}]'.format(re.escape(string.punctuation)))
        filtered_tokens = filter(None, [pattern.sub('', token) for token in tokens])
        filtered_text = ' '.join(filtered_tokens)
        
        return filtered_text
    
    def remove_stopwords(self, text):
        tokens = self.tokenize_text(text)
        filtered_tokens = [token for token in tokens if token not in self.stopword_list]
        filtered_text = ''.join(filtered_tokens)
        
        return filtered_text
    
    def normalize_corpus(self, corpus):
        normalized_corpus = []
        for text in corpus:
            text = ' '.join(jieba.lcut(text))
            normalized_corpus.append(text)
        
        return normalized_corpus

normalization = Normalization()
