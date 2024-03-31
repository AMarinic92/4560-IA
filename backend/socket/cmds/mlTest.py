from read import Read
from htmlparser import HtmlParser

html = Read().read_web_page("https://en.wikipedia.org/wiki/Royal_Maundy")
parser = HtmlParser(html)
links = parser.get_links()
links_with_words = parser.get_links_with_words(["Good Friday", "Developers", "Click here", "Help"])
print(links_with_words)



""" 
import imageCaptioning
import tensorflow as tf
from transformers import AutoTokenizer, TFAutoModelForTokenClassification, pipeline

pipe = pipeline("image-classification", model="cafeai/cafe_aesthetic")
result = pipe("https://static.wikia.nocookie.net/warhammer40k/images/5/55/AnkhoftheTriarch9thEdition.jpg/revision/latest/scale-to-width-down/1000?cb=20200925173557")
print(result)
 """
'''
tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model = TFAutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")

nlp = pipeline("ner", model=model, tokenizer=tokenizer)
testIn = "The first match between the association football teams of Scotland and Wales took place on 25 March 1876 at Hamilton Crescent, Partick, Scotland. The fixture was organised by Llewelyn Kenrick, who had founded the Football Association of Wales only a few weeks earlier. The Welsh team was selected after trial matches were held at the Racecourse Ground in Wrexham, Wales. Scotland, the more experienced team, dominated the match and had several chances to score in the first half. They had a goal disallowed after scoring directly from a corner kick, before taking the lead after 40 minutes through John Ferguson. In the early stages of the second half, Wales attempted to play more openly to find a goal, but the Scottish side took advantage of their opponent's inexperience and scored two further goals. Scotland added a fourth through Henry McNeil and claimed a victory in front of a crowd of around 17,000 people, a record for an international fixture at the time."
result = nlp(testIn)
print(result)
'''