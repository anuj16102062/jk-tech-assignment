from flask import Blueprint, request, jsonify
from database import db_session
from models import Document
from embeddings.generator import generate_embedding

ingestion_blueprint = Blueprint('ingestion', __name__)

@ingestion_blueprint.route('/upload', methods=['POST'])
def upload_document():
    data = request.json
    if not data or 'content' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    content = data['content']
    title = data.get('title', 'Untitled')
    
    # Generate embeddings
    embedding = generate_embedding(content)
    
    # Store in database
    new_document = Document(title=title, content=content, embedding=embedding)
    db_session.add(new_document)
    db_session.commit()
    
    return jsonify({'message': 'Document uploaded successfully', 'id': new_document.id})
