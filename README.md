---
title: 3.3 - Group B3 - Capstone Project
emoji: 🚀
colorFrom: green
colorTo: purple
sdk: gradio
sdk_version: '6.20.0'
python_version: '3.13'
app_file: app.py
pinned: false
short_description: KWK AI/ML Capstone · Camp 3.3 · Group B3 · Summer 2026
---

This Space was created for the KWK AI/ML capstone project. Happy building!

# **Budget Buddy**

This tool simplifies financial literacy and helps young adults make informed decisions and stay updated with financial terms. 💸
Created to help people tackle common misunderstanding and improve their understanding of money to help them make better financial decisions.


🤗 **Originally built as a Hugging Face Space:** https://huggingface.co/spaces/kode-with-klossy/3.3-groupB3-capstone 

> ⚠️ Note: This Space is no longer live. The code in this repo is the full project.

<img width="1402" height="729" alt="image" src="https://github.com/user-attachments/assets/6802dc1b-a7a0-4cc1-9cdf-733331367040" />


## What it does

- There are interactive tabs in the chatbot labeled "Investing", "Budgeting" & "Credit". Based on the financial_literacy_knowledge_base we created, most of of the information we found was divided into these three categories. When you click one of the buttons (enabled by the "examples" parameter in gr.ChatInterface), the chatbot provides a quick summary of what (button) is about. Afterwards the user can continue the chat and ask questions relating to that topic.
- The user can also type in the questions they want to ask to the chatbot, they aren't only restricted to the example prompts. If the question isn't found in the knowledge base, then the LLM will still try it's best to answer the question based on the information it has and based on when it was last updated
- The tabs at the bottom (Resources & Budget Tracker) allow the users to have more access to more helpful information. In the Resources Tabs, there are links users can access to look into more information and lessons on Khan Academy. Additionally, the Budget Tracker tab allows the user to have access to a Budget Tracker that allows them to track their finances for a year (implemented using HTML). 
-----------------------------------------------------------------------------------------------------------------------------------------------------
## Built with

- **Python**
- **Pytorch** — allows us to work with tensors
- **HTML** — for links and inserting an interactive version of the Budget Tracker (UI Features)
- **Gradio** — the interface
- **Hugging Face Inference Providers** — the AI model: meta-llama/Llama-3.1-8B-Instruct
- **Sentence Transformers** — necessary to convert text into vector representation (embeddings) that capture the meaning of a word to understand it's context to understand if a word is being used in a positive or negative connotation. This is determined with cosine similarity (the closer 2 vector embeddings, the closer they are in meaning and/or context). 
-----------------------------------------------------------------------------------------------------------------------------------------------------
## What I learned

- Token: Acts a digital pass to verfiy identity on HF platform and let code download AI models, use cloud tools and upload filed (txt. files and image .png)
- Building the Chatbot (Incorporate Semantic Search & RAG):
  Semantic Search
      1. Download the txt.file
      2. preprocess_text function: Get's rid of unnecessary spaces and symbols and adds this text to a cleaned_chunks list (we also need to use the strip method twice because the first time strips the whole text and then the next time strips each sentence 
      3. create_embeddings function: Load a pre-trained sentence transformer model (meta-llama/Llama-3.1-8B-Instruct) where the model uses the encode method to take in the text_chunks parameter and maps every chunk into vectors (aka the chunk_embeddings) to capture semantic meaning. Then it takes the shape of the chunk_embeddings (returns a tuple like torch.Size ([8,384]) to demonstrate the size of the 2D tensor
      4. get_top_chunks function: Find the most relevant text chunks for a given query, chunk_embeddings, and text_chunks. Normalize (to scale the lengths of the vectors to 1 while keep thing the direction the same to calculate cosine similarity) the query_embedding & the chunk_embedding and store them as new variables. Then perform matrix multiplication using the .matmul method from pytorch. Then take the top 3 indices (the indexes of sentences with the highest similarity scores with the query) and store them in top_chunks.
  
RAG
      set a variable called rag_info to the get_top_chunks function and call it. Then make a system_message variable let the chatbot know it's goal using the rag_info variable
-----------------------------------------------------------------------------------------------------------------------------------------------------
- Fixing the UI & Implementing Design Choices:
      1. Create a custom theme (gr.themes.Soft), making the body_background a lighter color than the chatbot's background allowed for a contrast and easier viewing of the words. 
      2. Use the blocks method in gradio allows us to implement elements on interface an include the custom theme and image using gr.Image. Then, using gr.ChatInterface, using "examaples" parameters allowed us to use example prompts for the user to press on the chatbot UI. 
      3.Using HTML inside gr.Tab:
          - <div style: Puts the contents on the UI with the features included the color, font, & padding
          - <a href="..." target="_blank">: Creates clickable links (also, target = "_blank" forces a new tab to open when clicked)
          - <iframe>: Embeds another webpage directly inside the page; the /preview shows a read-only preview of Google sheet
          - gr.Markdown: Creates clickable link from format ([Name](Link))
-----------------------------------------------------------------------------------------------------------------------------------------------------
## About

Built at [Kode With Klossy](https://www.kodewithklossy.com) AI/ML Camp,
Summer 2026, by Ananya Kantareddy, Avani Sathe, Camila Salguero, Emily Suriel, Yuri Hiraiwa.
