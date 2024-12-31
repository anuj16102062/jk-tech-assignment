# from transformers import pipeline

# # Load a pipeline for embedding and Q&A
# embedding_model = pipeline('feature-extraction', model='sentence-transformers/all-MiniLM-L6-v2')
# qa_model = pipeline('question-answering')

# def generate_embedding(text):
#     return embedding_model(text)[0]

# def generate_answer(question, embeddings):
#     # Mock RAG logic: Concatenate embeddings and use Q&A model
#     flattened_embeddings = [str(item) for sublist in embeddings for item in (sublist if isinstance(sublist, list) else [sublist])]

#     # Join the embeddings to form the context
#     context = " ".join(flattened_embeddings)
#     result = qa_model(question=question, context=context)
#     return result['answer']


#####
from flask import Flask, request, jsonify
import grok
from sklearn.metrics.pairwise import cosine_similarity

# Grok client initialization
client = grok.GrokClient(api_key="your_grok_api_key")


# Ingest a document and generate embeddings
def ingest_document(document):
    embedding = client.embed_document(document["content"])
    return embedding

# Generate a question embedding
def generate_question_embedding(question):
    return client.embed_text(question)

# Calculate cosine similarity
def get_most_relevant_document(question_embedding, document_embedding):
    similarity = cosine_similarity([question_embedding], [document_embedding])
    return similarity[0][0]

# Generate an answer based on context
def generate_answer(question, document_content):
    context = f"Question: {question}\nContext: {document_content}"
    return client.generate_answer(context)