# Code from https://huggingface.co/Salesforce/blip-image-captioning-base

import requests
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
import tensorflow as tf

processor = tf.BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = tf.BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base").to("cuda")

def imageCaption(img_url):

    raw_image = Image.open(requests.get(img_url, stream=True).raw).convert('RGB')

    # conditional image captioning
    text = "a photography of"
    inputs = processor(raw_image, text, return_tensors="pt").to("cuda")

    out = model.generate(**inputs)
    print(processor.decode(out[0], skip_special_tokens=True))
    # >>> a photography of a woman and her dog

    # unconditional image captioning
    inputs = processor(raw_image, return_tensors="pt").to("cuda")

    out = model.generate(**inputs)
    print(processor.decode(out[0], skip_special_tokens=True))
