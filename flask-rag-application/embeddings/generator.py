from transformers import pipeline

# Load a pipeline for embedding and Q&A
embedding_model = pipeline('feature-extraction', model='sentence-transformers/all-MiniLM-L6-v2')
qa_model = pipeline('question-answering')

def generate_embedding(text):
    return embedding_model(text)[0]

def generate_answer(question, embeddings):
    # Mock RAG logic: Concatenate embeddings and use Q&A model
    flattened_embeddings = [str(item) for sublist in embeddings for item in (sublist if isinstance(sublist, list) else [sublist])]

    # Join the embeddings to form the context
    context = " ".join(flattened_embeddings)
    result = qa_model(question=question, context=context)
    return result['answer']
