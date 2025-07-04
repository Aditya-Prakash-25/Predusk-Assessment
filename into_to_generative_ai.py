# -*- coding: utf-8 -*-
"""Into to Generative AI.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rpWyLb5OPNOL6mJcIPpAtx5XoCeTotHq
"""

# generate.py
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Load pre-trained GPT-2 (small)
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Ensure model is in evaluation mode and on appropriate device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
model.eval()

# Prompt
prompt = "Once upon a time"
input_ids = tokenizer.encode(prompt, return_tensors='pt').to(device)

# Generation settings
max_tokens = 50
top_k = 50

# Generate with temperature 0.7
output_07 = model.generate(
    input_ids,
    max_length=input_ids.shape[1] + max_tokens,
    do_sample=True,
    top_k=top_k,
    temperature=0.7
)

# Generate with temperature 1.0
output_10 = model.generate(
    input_ids,
    max_length=input_ids.shape[1] + max_tokens,
    do_sample=True,
    top_k=top_k,
    temperature=1.0
)

# Decode outputs
text_07 = tokenizer.decode(output_07[0], skip_special_tokens=True)
text_10 = tokenizer.decode(output_10[0], skip_special_tokens=True)

# Save to text file
with open("generated_outputs.txt", "w") as f:
    f.write("=== Output with temperature 0.7 ===\n")
    f.write(text_07 + "\n\n")
    f.write("=== Output with temperature 1.0 ===\n")
    f.write(text_10 + "\n")

