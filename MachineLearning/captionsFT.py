import tensorflow as tf
import numpy as np
from transformers import pipeline, AutoProcessor, TFAutoModel, TFBlipForConditionalGeneration, AutoTokenizer, DataCollatorWithPadding, TrainingArguments, Trainer
from datasets import load_dataset, load_metric
from concurrent.futures import ThreadPoolExecutor
from functools import partial
import io
import urllib

import PIL.Image

from datasets.utils.file_utils import get_datasets_user_agent


checkpoint = 'Salesforce/blip-image-captioning-base'
# model = TFAutoModelForSequenceClassification.from_pretrained(checkpoint)
loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
# model.compile(optimizer='', loss=loss)

## Load in the dataset to fine tune model, This case conceptual captions

USER_AGENT = get_datasets_user_agent()



def fetch_single_image(image_url, timeout=None, retries=0):
    for _ in range(retries + 1):
        try:
            request = urllib.request.Request(
                image_url,
                data=None,
                headers={"user-agent": USER_AGENT},
            )
            with urllib.request.urlopen(request, timeout=timeout) as req:
                image = PIL.Image.open(io.BytesIO(req.read()))
            break
        except Exception:
            image = None
    return image


def fetch_images(batch, num_threads, timeout=None, retries=0):
    fetch_single_image_with_args = partial(fetch_single_image, timeout=timeout, retries=retries)
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        batch["image"] = list(executor.map(fetch_single_image_with_args, batch["image_url"]))
    return batch


num_threads = 20
dset = load_dataset("conceptual_captions", trust_remote_code=True)
dset = dset.map(fetch_images, batched=True, batch_size=100, fn_kwargs={"num_threads": num_threads})

# load model

checkpoint = "Salesforce/blip-image-captioning-base"
pipe = pipeline("image-to-text", model = checkpoint)
# tokenizer = AutoTokenizer.from_pretrained(checkpoint)
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")

# model = TFAutoModel.from_pretrained(checkpoint)
model = TFBlipForConditionalGeneration.from_pretrained(checkpoint)

## 

training_args = TrainingArguments("test-trainer", evaluation_strategy="epoch")

def compute_metrics(eval_preds):
    logits, labels = eval_preds
    predictions = np.argmax(logits, axis=-1)
    return metric.compute(predictions=predictions, references=predictions.label_ids)

trainer = Trainer(
    model,
    training_args,
    train_dataset= dset["train"],
    eval_dataset= dset["validation"],
    compute_metrics=compute_metrics
)

predictions = trainer.predict()
print(predictions.predictions.shape, predictions.label_ids.shape)

metric = load_metric("conceptual_captions")
# preds = np.argmax(predictions.predictions, axis=-1)
# metric.compute(predictions=preds, references=predictions.label_ids)

trainer.train()








dataset = 'conceptual_captions'
raw_datasets = load_dataset(dataset)

tokenizer = AutoTokenizer.from_pretrained("Salesforce/blip-image-captioning-base")

def tokenize_function(example):
  return tokenizer(
      example["image_url"], example["caption"],truncation=True, max_length = 1024
  )

tokenized_datasets = raw_datasets.map(tokenize_function)




# model.fit(
#     tf_train_dataset,
#     validation_data=tf_validation_dataset,
#     epochs=3
#     )
