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

with open("financial_literacy_knowledge_base.txt", "r", encoding="utf-8") as file:                 #open water_cycle text in "read" mode w/ encoding utf-8
  # Read the entire contents of the file and store it in a variable
  knowledge_base = file.read()                                                

# Print the text below
print(knowledge_base)

#preprocess function
def preprocess_text(text):
  # Strip extra whitespace from the beginning and the end of the text
  cleaned_text = text.strip()

  # Split the cleaned_text by every newline character (\n)
  chunks = cleaned_text.split("\n")            #Each line is a new sentence and it splits the chunks per line

  # Create an empty list to store cleaned chunks
  cleaned_chunks = []

  # Write your for-in loop below to clean each chunk and add it to the cleaned_chunks list
  for chunk in chunks:
    stripped_chunk = chunk.strip()
    cleaned_chunks.append(stripped_chunk)

  # Print cleaned_chunks
  print(cleaned_chunks)

  # Print the length of cleaned_chunks
  print(len(cleaned_chunks))
 
  # Return the cleaned_chunks
  return cleaned_chunks

# Call the preprocess_text function and store the result in a cleaned_chunks variable
cleaned_chunks = preprocess_text(knowledge_base) 

# Load the pre-trained embedding model that converts text to vectors        #help convert text into vectors (384 dimensional vectors)
model = SentenceTransformer('all-MiniLM-L6-v2')

#create_embeddings function
def create_embeddings(text_chunks):
  # Convert each text chunk into a vector embedding and store as a tensor
  chunk_embeddings = model.encode(text_chunks, convert_to_tensor=True) # Replace ... with the text_chunks list
    
  # Print the chunk embeddings
  print (chunk_embeddings)

  # Print the shape of chunk_embeddings
  print(chunk_embeddings.shape)

  # Return the chunk_embeddings
  return chunk_embeddings

# Call the create_embeddings function and store the result in a new chunk_embeddings variable                           #8 chunks of text (8 rows & 34 columns)
chunk_embeddings = create_embeddings(cleaned_chunks) 

# Define a function to find the most relevant text chunks for a given query, chunk_embeddings, and text_chunks
def get_top_chunks(query, chunk_embeddings, text_chunks):
  # Convert the query text into a vector embedding
  query_embedding = model.encode(query, convert_to_tensor = True) # Complete this line

  # Normalize the query embedding to unit length for accurate similarity comparison
  query_embedding_normalized = query_embedding / query_embedding.norm()

  # Normalize all chunk embeddings to unit length for consistent comparison
  chunk_embeddings_normalized = chunk_embeddings / chunk_embeddings.norm(dim=1, keepdim=True)

  # Calculate cosine similarity between all chunks and the query using matrix multiplication
  similarities = torch.matmul(chunk_embeddings_normalized, query_embedding_normalized) # Complete this line       Order matters for matrix multiplcation (inside numbers need to be the same)

  # Print the similarities
  print(similarities)

  # Find the indices of the 3 chunks with highest similarity scores
  top_indices = torch.topk(similarities, k=3).indices

  # Print the top indices
  print(top_indices)

  # Create an empty list to store the most relevant chunks
  top_chunks = []

  # Loop through the top indices and retrieve the corresponding text chunks
  for i in top_indices:
    relevant_info = text_chunks[i]
    top_chunks.append(relevant_info)

  # Return the list of most relevant chunks
  return top_chunks

client = InferenceClient("Qwen/Qwen2.5-7B-Instruct", bill_to="kode-with-klossy")

#respond function
def respond(message, history):

    rag_info = get_top_chunks(message, chunk_embeddings, cleaned_chunks)
    system_message = f"You are a friendly chatbot who uses {rag_info} to answer questions about financial literacy."
    
    messages = [{"role": "system", "content": system_message}]

    if history:
        messages.extend(history)

    messages.append({"role": "user", "content": message})

    response = client.chat_completion(
        messages,
        max_tokens=2000
    )

    return response.choices[0].message.content.strip()
    
def display_image():
    return "budgetbuddy.png"
    
custom_theme = (
    gr.themes.Soft(primary_hue = "green", radius_size = "lg")
    .set(
        body_background_fill="#ADE0AE",
        body_background_fill_dark="#ADE0AE",

        #background_fill_primary="#ADE0AE",
        #background_fill_primary_dark="#ADE0AE",

        background_fill_secondary="#124a34",
        background_fill_secondary_dark="#124a34",
    )
)


with gr.Blocks(theme=custom_theme) as chatbot:
    gr.Image(display_image())

    gr.HTML("""
    <h1 style="color:#4CAF50; font-weight:bold; text-align:center;">
        Introducing the Budget Buddy!
    </h1>
    """)
    
    gr.ChatInterface(
        respond,
        #title="Introducing the Budget Buddy! 💵",
        textbox=gr.Textbox(placeholder="Ask Me Anything!"),
        description="This tool simplifies financial literacy and helps young adults make informed financial decisions. 💸",
        examples=["Investing", "Budgeting", "Credit"]
    )
    with gr.Tab("Resources"):  
        gr.HTML("""
        <div style="padding: 10px; font-family: sans-serif;">
            <h2 style="color: #124a34;">📚 Useful Financial Literacy Resources</h2>
            <p style= "color: #124a34;">Check out these helpful links to learn more:</p>
            <ul style="line-height: 1.8;">
                <li><a href="https://www.investopedia.com/terms/f/financial-literacy.asp" target="_blank" style="color: #0d47a1; font-weight: bold;">Investopedia - Financial Literacy Guide</a></li>
                <li><a href="https://www.schwab.com/learn/story/what-is-financial-literacy" target="_blank" style="color: #0d47a1; font-weight: bold;">Consumer Financial Protection Bureau (CFPB)</a></li>
                <li><a href="https://blogs.uofi.uillinois.edu/view/7550/176801781" target="_blank" style="color: #0d47a1; font-weight: bold;">Khan Academy - Finance & Capital Markets</a></li>
                <li><a href="https://www.cnbc.com/personal-finance/" target="_blank" style="color: #0d47a1; font-weight: bold;">MyMoney.gov</a></li>
            </ul>
        </div>
        """)


    with gr.Tab("Budget Tracker"):
        gr.HTML("""
            <iframe
                src="https://docs.google.com/spreadsheets/d/1Ok2AgQ_YlXGnw-9XP0SvMvMqTCiNcQhvMNuv5KdcsuA/preview"
                width="100%"
                height="700"
                style="border:none;">
            </iframe>
        """)

        gr.Markdown("""

[Open Budget Tracker](https://docs.google.com/spreadsheets/d/1Ok2AgQ_YlXGnw-9XP0SvMvMqTCiNcQhvMNuv5KdcsuA/edit?usp=sharing)
""")
chatbot.launch()


# TODO: This is just a starting point! Customize the system prompt,
# the model, and the interface to make this project your own!
