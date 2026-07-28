import gradio as gr
from huggingface_hub import InferenceClient
from sentence_transformers import SentenceTransformer  #library that's necessary to tconvert text into vector representation (embeddings) that capture meaning
import torch #pytorch: allows us to work with tensors

# This is the same pattern from the Generative AI lesson! It uses the
# Inference Provider API to send your messages to an AI model and get
# a response back. Swap out the model below for a different one if
# you want to experiment!
#
# Note: if this Space doesn't already have one, you'll need to add an
# HF_TOKEN secret in the Space's Settings tab for this to work
# (Settings -> Variables and secrets -> New secret).
with open("water_cycle.txt", "r", encoding="utf-8") as file:                 #open water_cycle text in "read" mode w/ encoding utf-8
  # Read the entire contents of the file and store it in a variable
  water_cycle_text = file.read()                                                

# Print the text below
print(water_cycle_text)


client = InferenceClient("Qwen/Qwen2.5-7B-Instruct")


def respond(message, history):
    messages = [{"role": "system", "content": "You are a friendly chatbot."}]

    if history:
        messages.extend(history)

    messages.append({"role": "user", "content": message})

    response = client.chat_completion(
        messages,
        max_tokens=100
    )

    return response.choices[0].message.content.strip()

chatbot = gr.ChatInterface(respond)

chatbot.launch()


# TODO: This is just a starting point! Customize the system prompt,
# the model, and the interface to make this project your own!
