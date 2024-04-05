import tensorflow as tf
import numpy as np
from transformers import DefaultDataCollator, pipeline, BlipProcessor, BlipImageProcessor, TFAutoModel, TFBlipForConditionalGeneration, AutoTokenizer, TFBertTokenizer, TrainingArguments, Trainer, DataCollatorWithPadding
from datasets import load_dataset, load_metric, get_dataset_split_names, Image, Dataset, Features, ClassLabel, Value
from concurrent.futures import ThreadPoolExecutor
from functools import partial
import io
import urllib

import PIL.Image

from datasets.utils.file_utils import get_datasets_user_agent


checkpoint = 'Salesforce/blip-image-captioning-large'


## Load in the dataset to fine tune model, This case conceptual captions

# USER_AGENT = get_datasets_user_agent()



# def fetch_single_image(image_url, timeout=None, retries=0):
#     for _ in range(retries + 1):
#         try:
#             request = urllib.request.Request(
#                 image_url,
#                 data=None,
#                 headers={"user-agent": USER_AGENT},
#             )
#             with urllib.request.urlopen(request, timeout=timeout) as req:
#                 image = PIL.Image.open(io.BytesIO(req.read()))
#             break
#         except Exception:
#             image = None
#     return image


# def fetch_images(batch, num_threads, timeout=None, retries=0):
#     fetch_single_image_with_args = partial(fetch_single_image, timeout=timeout, retries=retries)
#     with ThreadPoolExecutor(max_workers=num_threads) as executor:
#         batch["image"] = list(executor.map(fetch_single_image_with_args, batch["image_url"]))
#     return batch


# num_threads = 20
# dset = load_dataset("conceptual_captions", trust_remote_code=True)
# dset = dset.map(fetch_images, batched=True, batch_size=100, fn_kwargs={"num_threads": num_threads})
# tokenizer = TFAutoTokenizer.from_pretrained(checkpoint)
tokenizer = TFBertTokenizer.from_pretrained(checkpoint)
# processor = BlipImageProcessor.from_pretrained(checkpoint, return_tensors="tf")
processor = BlipProcessor.from_pretrained(checkpoint)

dset = load_dataset("imagefolder", data_dir="./trainTest", split="train", drop_labels=False)

def tokenize_function(example):
    return tokenizer(example["caption"])

def transforms(examples):
    examples["pixel_values"] = [image.convert("RGB").resize((100,100)) for image in examples["image"]]
    return examples

def process_function(example):
    return processor(example["image"], example["caption"])

# tokenized_dataset = dset.map(tokenize_function, batched=True)

tokenized_dataset = dset.map(process_function, batched=True)

# tokenized_dataset = tokenized_dataset.map(transforms, remove_columns=["image"], batched=True)

print(tokenized_dataset[0].keys())
print(tokenized_dataset['label'])
# print(tokenized_dataset[0]["pixel_values"])



#data_collator = DataCollatorWithPadding(tokenizer = tokenizer,return_tensors="np")
# data_collator = DefaultDataCollator(return_tensors="np")

# tf_dataset = tokenized_dataset.to_tf_dataset(
#     columns=['pixel_values', 'input_ids', 'attention_mask'],
#     label_cols='label',
#     batch_size=2,
#     collate_fn=data_collator,
#     shuffle=True
# )
features = Features({'image': Image(),
               'label':ClassLabel(num_classes=2), 
               'caption': Value(dtype='string', id=None)})
tf_dataset = Dataset.from_dict({"image":dset['image'], 
                                'label':dset['label'],
                                'caption':dset['caption']}, features=features)
print(tf_dataset)
tf_dataset = tf_dataset.with_format("tf",columns=["image","label, caption"], output_all_columns=True)

# print(tf_dataset)


# # load model

# pipe = pipeline("image-to-text", model = checkpoint)
# # tokenizer = AutoTokenizer.from_pretrained(checkpoint)
# processor = AutoProcessor.from_pretrained(checkpoint)

# model = TFAutoModel.from_pretrained(checkpoint)
model = TFBlipForConditionalGeneration.from_pretrained(checkpoint)

# ## 

# loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
model.compile(optimizer='adam')



model.fit(
    tf_dataset,
    validation_data=None,
    epochs=3
    )









# dataset = 'conceptual_captions'
# raw_datasets = load_dataset(dataset)

# tokenizer = AutoTokenizer.from_pretrained("Salesforce/blip-image-captioning-base")



