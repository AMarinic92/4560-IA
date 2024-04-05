import numpy as np
import torch
import torchvision
from torch.autograd import Variable
from pytorch2keras.converter import pytorch_to_keras
from transformers import AutoModelForImageClassification
from onnx import optimizer

model = AutoModelForImageClassification.from_pretrained("cafeai/cafe_aesthetic")

input_np = np.random.uniform(0, 1, (1, 10, 32, 32))
input_var = Variable(torch.FloatTensor(input_np))

# we should specify shape of the input tensor
k_model = pytorch_to_keras(model, input_var, [(10, 32, 32,)], verbose=True)  

print(k_model)