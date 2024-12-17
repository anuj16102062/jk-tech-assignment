from flask import Blueprint, request, jsonify
from database import db_session
from models import Document

selection_blueprint = Blueprint('selection', __name__)

@selection_blueprint.route('/list', methods=['GET'])
def list_documents():
    documents = db_session.query(Document).all()
    document_list = [{'id': doc.id, 'title': doc.title} for doc in documents]
    return jsonify({'documents': document_list})

@selection_blueprint.route('/select', methods=['POST'])
def select_documents():
    data = request.json
    document_ids = data.get('document_ids', [])

    if not document_ids:
        return jsonify({'error': 'No documents selected'}), 400

    # Simulate saving user selections (for simplicity)
    return jsonify({'message': f'{len(document_ids)} documents selected.'})
