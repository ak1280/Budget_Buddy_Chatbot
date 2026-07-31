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

## How it works

[Explain your project in a few sentences, in your own words. What happens
when a user types a message? Where does your chatbot get its knowledge?]

## Built with

- **Python**
- **Pytorch** — allows us to work with tensors
- **HTML** — for links and inserting an interactive version of the Budget Tracker (UI Features)
- **Gradio** — the interface
- **Hugging Face Inference Providers** — the AI model: meta-llama/Llama-3.1-8B-Instruct
- **Sentence Transformers** — necessary to convert text into vector representation (embeddings) that capture the meaning of a word to understand it's context to understand if a word is being used in a positive or negative connotation. This is determined with cosine similarity (the closer 2 vector embeddings, the closer they are in meaning and/or context). 

## What I learned

- Building the Chatbot (Semantic Search & RAG):
- Fixing the UI & Implementing Design Choices: 

[The hardest part of building this, and how you figured it out. This is the
part people actually read — don't skip it!]

## About

Built at [Kode With Klossy](https://www.kodewithklossy.com) AI/ML Camp,
Summer 2026, by Ananya Kantareddy, Avani Sathe, Camila Salguero, Emily Suriel, Yuri Hiraiwa.
