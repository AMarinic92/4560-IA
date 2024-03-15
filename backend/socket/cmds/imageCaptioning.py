import tensorflow as tf
from transformers import pipeline

class imageCap:
    def __init__(self,url):
        self.image_url =  url
        self.caption = ""
    
    def get_caption(self):
        captioner = pipeline("image-to-text",model="Salesforce/blip-image-captioning-base")
        self.caption = captioner(self.image_url)