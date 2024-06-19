import io
import torch
import streamlit as st
from PIL import Image
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer


def generate_image_description(image_content):
    model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
    feature_extractor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
    tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    max_length = 16
    num_beams = 4
    gen_kwargs = {"max_length": max_length, "num_beams": num_beams}

    if isinstance(image_content, str):  # Assuming image_content is a file path
        img = Image.open(image_content)
    elif isinstance(image_content, bytes):  # Assuming image_content is already bytes
        img = Image.open(io.BytesIO(image_content))
    elif isinstance(image_content, Image.Image):  # If it's already a PIL.Image.Image instance
        img = image_content
    else:
        raise ValueError("Unsupported image content type")

    if img.mode != "RGB":
        img = img.convert('RGB')

    pixel_values = feature_extractor(images=[img], return_tensors="pt").pixel_values.to(device)
    output_ids = model.generate(pixel_values, **gen_kwargs)
    description = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    return description
