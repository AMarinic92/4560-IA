import tensorflow as tf
from transformers import pipeline

captioner = pipeline("image-to-text",model="Salesforce/blip-image-captioning-base")
out = captioner("https://static.wikia.nocookie.net/mtgsalvation_gamepedia/images/5/5e/Necron.jpg/revision/latest?cb=20220825124248")
print(out)