import tensorflow as tf
from transformers import pipeline
from htmlparser import HtmlParser
from read import Read


class KeyWorderFinder:
    def __init__(self,url):
        self.html = Read().read_web_page(url)
        self.parser = HtmlParser(self.html)
        self.tags = self.parser.get_page_words()
        self.words = []


    def get_summary(self,min_words, max_words):
        for tag in self.tags:
            text = tag.get_text()
            if(len(text.split(" ")) > max_words):
                self.words.append(text)
        wordlist = self.words 
        summarizer = pipeline("summarization")
        return summarizer(wordlist, min_length=min_words, max_length=max_words)
    
    def get_token_class(self):
        for tag in self.tags:
            text = tag.get_text()
            self.words.append(text)
        #tokenizer = pipeline("token-classification",model="ml6team/keyphrase-extraction-kbir-inspec",from_pt=True)  #not as nice as an output can tinker more
        tokenizer = pipeline("token-classification")
        keyphrases = tokenizer(self.words)
