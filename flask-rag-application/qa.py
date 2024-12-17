from flask import Blueprint, request, jsonify
from database import db_session
from models import Document
from embeddings.generator import generate_answer
from sqlalchemy import func

qa_blueprint = Blueprint('qa', __name__)

@qa_blueprint.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    if not data or 'question' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    question = data['question']
    document_ids = data.get('document_ids', [])

    # Fetch relevant documents
    query = db_session.query(Document)
    if document_ids:
        query = query.filter(Document.id.in_(document_ids))
    
    documents = query.all()

    if not documents:
        return jsonify({'error': 'No relevant documents found'}), 404
    
    # Retrieve embeddings and answer
    embeddings = [doc.embedding for doc in documents]
    answer = generate_answer(question, embeddings)
    
    return jsonify({'answer': answer})
